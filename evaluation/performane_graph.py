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
            if(load>25):
                loads.append(load)
                times.append(time)
    
    median = loads[int(len(loads)/2)]
    if(len(loads)<2): median = loads[0]
    elif(type(len(loads)/2)==float): median = (loads[int(len(loads)/2-0.5)]+loads[int(len(loads)/2+0.5)])/2
    avg_size = sum(loads)/len(loads)
    x = [*range(times[0],times[-1],20),times[-1]]
    y1 = [avg_size for _ in x]
    y2 = [median for _ in x]

    plt.plot(times,loads)
    plt.plot(x,y1,"-r")
    plt.plot(x,y1,"--g")
    plt.legend(["performances", "avg performance", "median performance"])
    plt.xlabel("Time(sec)")
    plt.xticks()
    plt.ylabel("Load on CPU(%)")
    plt.show()

