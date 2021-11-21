import matplotlib.pyplot as plt
import sys


sizeMap = {}
if len(sys.argv)>1:
    with open(sys.argv[1],"r") as file:
        lines = file.readlines()
        for line in lines:
            if "segment" in line:
                segmentNumber = int(line.split(" ")[-1].split("_")[-1].split(".")[0])
                size = line.split("vagrant vagrant")[-1].strip().split(" ")[0]
                size = float(size)/(1000*1000)
                if size > 0: sizeMap[segmentNumber] = size
    
    segments,sizes = ([],[])
    for segment,size in sizeMap.items():
        segments.append(segment)
        sizes.append(size)
    median = sizes[int(len(sizes)/2)]
    if(type(len(sizes)/2)==float): median = (sizes[int(len(sizes)/2-0.5)]+sizes[int(len(sizes)/2+0.5)])/2
    avg_size = sum(sizes)/len(sizes)
    sortedSegments = sorted(segments)
    x = [*range(sortedSegments[0],sortedSegments[-1],20),sortedSegments[-1]]
    y1 = [avg_size for _ in x]
    y2 = [median for _ in x]

    plt.scatter(segments,sizes)
    plt.plot(x,y1,"-r")
    plt.plot(x,y1,"--g")
    plt.legend(["segments", "avg segment size", "median segment size"])
    plt.xlabel("segment numbers")
    plt.xticks()
    plt.ylabel("file size(MB)")
    plt.show()

