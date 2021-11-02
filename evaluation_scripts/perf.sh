# !/bin/bash

intfs=();
innet=();
outnet=();
processes=();

for var in "$@"
do
    first="$var";
    if [[ $first == *"i-"* ]]; then
        second="";
        first=${first/i-/$second};
        echo "Got interface $first";
        intfs+=("$first");
        innet+=(0);
        outnet+=(0);
    fi

    if [[ $first == *"p-"* ]]; then
        first=${first/p-/$second};
        echo "Got process $first";
        processes+=("$first");
    fi
done
echo processes: ${processes[@]}
echo intfs: ${intfs[@]}
echo innet: ${innet[@]}
echo outnet: ${outnet[@]}

ind=0;
prnt="";
prnt2="";
for var in ${!intfs[*]}
do
    innow="$(</sys/class/net/${intfs[$var]}/statistics/rx_bytes)"; 
    innet[$var]=$innow;
    outnow="$(</sys/class/net/${intfs[$var]}/statistics/tx_bytes)"; 
    outnet[$var]=$outnow;
    prnt="$prnt\t\t${intfs[$var]:0:6}";
done

for var in ${!processes[*]}
do
    prnt2="$prnt2\t\t${processes[$var]}";
done

echo -e "Sec\t\tNetw$prnt\t\tCPU$prnt2";
interval=2;
loopCount=0;
numCPU=4;
while true; do 
    STARTTIME=$(date +%s)
    print="";
    intotal=0;
    for var in ${!intfs[*]}
    do
        inold=${innet[$var]};
        innow="$(</sys/class/net/${intfs[$var]}/statistics/rx_bytes)"; 
        inval="$((($innow-$inold)/131072))";
        intotal=$(($intotal+$inval));
        innet[$var]=$innow;

        outold=${outnet[$var]};
        outnow="$(</sys/class/net/${intfs[$var]}/statistics/tx_bytes)"; 
        outval="$((($outnow-$outold)/131072))";
        outtotal=$(($outtotal+$outval));
        outnet[$var]=$outnow;

        print="$print\t\t$inval/$outval";
    done
    
    # val="$(top -b -n 2 -d 0.2 | tail -1 | awk '{print $9}')"
    val=0
    # $(echo $[100-$(vmstat 1 2|tail -1|awk '{print $15}')]);
    print="$print\t\t$val";

    for var in ${!processes[*]}
    do
        val="$(top -b -n 2 -d 0.2 -p ${processes[$var]} | tail -1 | awk '{print $9}')"
        # val=0;
        # int=${val%,*}
	if [ "$val" = "%CPU" ];then
		val=0
	else
		int=$( printf "%.0f" $val )
                val=$(($int / $numCPU))
	fi
        print="$print\t\t$val";
    done
    ENDTIME=$(date +%s)
    # echo "It takes $(($ENDTIME - $STARTTIME)) seconds to complete this task..."
    echo -e "$(($loopCount*$interval))\t\t$intotal/$outtotal$print";
    sleepFor=$(($interval - $(($ENDTIME - $STARTTIME))))
    if (( $sleepFor > 0 )); then
#         echo "Sleep for $sleepFor seconds"
        sleep $sleepFor
    fi 
    loopCount=$(($loopCount+1))
done
