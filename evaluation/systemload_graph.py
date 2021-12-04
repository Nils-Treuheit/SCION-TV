import matplotlib.pyplot as plt
import sys


loads = []
times = []
if len(sys.argv)>1:
    with open(sys.argv[1],"r") as file:
        lines = file.readlines()[7:]
        for line in lines:
            load = int(line.split("\t\t")[-1].strip())
            time = int(line.split("\t\t")[0].strip())
            if(load>15):
                loads.append(load)
                times.append(time)
    
    median = loads[int(len(loads)/2)]
    if(len(loads)<2): median = loads[0]
    elif(type(len(loads)/2)==float): median = (loads[int(len(loads)/2-0.5)]+loads[int(len(loads)/2+0.5)])/2
    avg_load = sum(loads)/len(loads)
    trans_avg = sum(list(filter(lambda x: x>avg_load,loads)))/len(list(filter(lambda x: x>avg_load,loads)))
    print("AVG: "+str(avg_load))
    print("Active Transcoding AVG: "+str(trans_avg))
    print("Median: "+str(median))   
     
    x = [*range(times[0],times[-1],20),times[-1]]
    y1 = [avg_load for _ in x]
    y2 = [median for _ in x]
    y3 = [trans_avg for _ in x]

    plt.plot(times,loads)
    plt.plot(x,y1,"-",color="tab:orange")
    plt.plot(x,y2,"--g")
    plt.plot(x,y3,"-r")
    plt.legend(["system load", "avg system load", "median system load", "active transcoding avg load"])
    plt.xlabel("Time(sec)")
    plt.xticks()
    plt.ylabel("Load on CPU(%)")
    plt.show()

