from glob import glob
import numpy as np

segment_size_files = glob("data_collection/*_size.log")
transco_perf_files = glob("data_collection/*_perf.log")


avg_load_file = open("avg_loads.gen_log","w")
std_load_file = open("std_loads.gen_log","w")
for filename in transco_perf_files:
    avg_load_file.write(filename+"\n")
    std_load_file.write(filename+"\n")
    loads,times = ([],[])
    with open(filename,"r") as file:
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
    avg_load_file.write("avg_load "+str(avg_load)+" %\ntrans_avg "+str(trans_avg)+" %\n")
    std = np.std(loads)
    std_load_file.write("std "+str(std)+" %\n")
    print("\n"+filename+":")
    print("median: "+str(median))
    print("avg_load: "+str(avg_load))
    print("avg_active_load: "+str(trans_avg))
    print("min: "+str(min(loads)))
    print("max: "+str(max(loads)))
    print("std: "+str(std))
avg_load_file.close()
std_load_file.close()



avg_size_file = open("avg_size.gen_log","w")
std_size_file = open("std_size.gen_log","w")
for filename in segment_size_files:
    avg_size_file.write(filename+"\n")
    std_size_file.write(filename+"\n")
    sizeMap = {}
    with open(filename,"r") as file:
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
    avg_size_file.write("avg_size "+str(avg_size)+" MB\n")
    std = np.std(sizes)
    std_size_file.write("std "+str(std)+" MB\n")
    print("\n"+filename+":")
    print("median: "+str(median))
    print("avg_load: "+str(avg_size))
    print("min: "+str(min(sizes)))
    print("max: "+str(max(sizes)))
    print("std: "+str(std))
avg_size_file.close()
std_size_file.close()