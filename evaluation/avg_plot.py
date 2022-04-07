from glob import glob
import math, numpy as np
from os import getcwd
from sys import argv
import matplotlib.pyplot as plt
import matplotlib.patches as mlpat
from mpl_toolkits.mplot3d import Axes3D

path = argv[0].strip("\\avg_plot.py")+"/data_collection/"
files = glob(path+"avg_*.gen_log")
print(path)

keys,active_loads,loads,std_loads,perfs,sizes,std_sizes = ([],[],[],[],[],[],[])
for filename in files:
    enc_format = (filename.split(".")[0].split("_")[-1])
    file = open(filename,"r")
    lines = file.readlines()
    for line_count,line in enumerate(lines):
        if line_count%7==0: 
            keys.append((enc_format + "_" +line.strip()))
        elif line_count%7==1:
            perfs.append(float(line.split(" ")[1]))
        elif line_count%7==2:     
            active_loads.append(float(line.split(" ")[1]))
        elif line_count%7==3:     
            loads.append(float(line.split(" ")[1]))
        elif line_count%7==4:     
            std_loads.append(float(line.split(" ")[1]))    
        elif line_count%7==5:     
            sizes.append(float(line.split(" ")[1]))
        elif line_count%7==6:     
            std_sizes.append(float(line.split(" ")[1]))
    file.close()

avg_load = (sum(loads)+sum(active_loads))/(len(loads)+len(active_loads))
avg_size = sum(sizes)/len(sizes)
avg_perf = sum(perfs)/len(perfs)
load_ticks = [*range(0,101,10)]
size_ticks = [0,1,*range(5,math.ceil(max(sizes)+max(sizes)/8+10),10)]
size_labels = [0,"1   \n",*range(5,math.ceil(max(sizes)+max(sizes)/8+10),10)]
perf_ticks = sorted([*range(0,71,10),55,45,75])
perf_labels = [*range(0,50,10),"",50,"",60,"",75]
colors = ["cornflowerblue","tab:blue","mediumslateblue","deepskyblue","aqua","tab:red","tab:orange","tab:green","tab:olive","lime","violet","hotpink","tab:brown","tab:grey"]
#cmaps = ["Blues","cool","Reds","Oranges","Greens","summer","Purples","spring","copper","Greys"]

plt.figure(0)
legend = []
plt.scatter(avg_load,avg_size,c='k',alpha=0.2)
for idx in range(len(keys)):
    x1 = np.zeros(len(size_ticks))+loads[idx]
    x2 = np.zeros(len(size_ticks))+active_loads[idx]
    y = np.zeros(len(load_ticks))+sizes[idx]
    plt.scatter(active_loads[idx],sizes[idx],c=colors[idx])
    plt.plot(x1,size_ticks,"-",color=colors[idx])
    plt.plot(x2,size_ticks,"--",color=colors[idx])
    plt.plot(load_ticks,y,"-",color=colors[idx])
    patch = mlpat.Patch(color=colors[idx], label=keys[idx])
    legend.append(patch)
plt.ylabel("AVG Size(MB)")
plt.xlabel("AVG Load(%)")
plt.yticks(size_ticks,size_labels)
plt.xticks(load_ticks)
plt.legend(handles=legend)
plt.subplots_adjust(left=0.075,bottom=0.075,top=0.97,right=0.97)

plt.figure(1)
legend = []
plt.scatter(avg_load,avg_perf,c='k',alpha=0.2)
for idx in range(len(keys)):
    x1 = np.zeros(len(perf_ticks))+loads[idx]
    x2 = np.zeros(len(perf_ticks))+active_loads[idx]
    y = np.zeros(len(load_ticks))+perfs[idx]
    plt.scatter(active_loads[idx],perfs[idx],c=colors[idx])
    plt.plot(x1,perf_ticks,"-",color=colors[idx])
    plt.plot(x2,perf_ticks,"--",color=colors[idx])
    plt.plot(load_ticks,y,"-",color=colors[idx])
    patch = mlpat.Patch(color=colors[idx], label=keys[idx])
    legend.append(patch)
plt.ylabel("AVG Performance(fps)")
plt.xlabel("AVG Load(%)")
plt.yticks(perf_ticks,perf_labels)
plt.xticks(load_ticks)
plt.legend(handles=legend)
plt.subplots_adjust(left=0.075,bottom=0.075,top=0.97,right=0.97)

plt.figure(2)
legend = []
plt.scatter(avg_perf,avg_size,c='k',alpha=0.2)
for idx in range(len(keys)):
    x = np.zeros(len(size_ticks))+perfs[idx]
    y = np.zeros(len(perf_ticks))+sizes[idx]
    plt.scatter(perfs[idx],sizes[idx],c=colors[idx])
    plt.plot(x,size_ticks,"-",color=colors[idx])
    plt.plot(perf_ticks,y,"-",color=colors[idx])
    patch = mlpat.Patch(color=colors[idx], label=keys[idx])
    legend.append(patch)
plt.ylabel("AVG Size(MB)")
plt.xlabel("AVG Performance(fps)")
plt.yticks(size_ticks,size_labels)
plt.xticks(perf_ticks,perf_labels)
plt.legend(handles=legend)
plt.subplots_adjust(left=0.075,bottom=0.075,top=0.97,right=0.97)

fig = plt.figure(3)
ax = plt.axes(projection='3d')
size_labels[1] = "\n     1"
legend = []
for idx in range(len(keys)):
    x,y,z = (np.arange(max(perfs[idx]-4,0),perfs[idx]+4,((perfs[idx]+4)-max(perfs[idx]-4,0))/20),
             np.arange(max(sizes[idx]-std_sizes[idx]/2,0),sizes[idx]+std_sizes[idx]/2,((sizes[idx]+std_sizes[idx]/2)-max(sizes[idx]-std_sizes[idx]/2,0))/20),
             np.arange(max(loads[idx]-std_loads[idx],0),min(active_loads[idx]+std_loads[idx],100),(min(active_loads[idx]+std_loads[idx],100)-max(loads[idx]-std_loads[idx],0))/20))
    x = np.hstack((x,np.flip(x),x,np.flip(x),x,np.flip(x),x,np.flip(x)))
    y = np.hstack((y,y,np.flip(y),np.flip(y),y,y,np.flip(y),np.flip(y)))
    z = np.hstack((z,z,z,z,np.flip(z),np.flip(z),np.flip(z),np.flip(z)))
    x,y,z = np.meshgrid(x,y,z)
    x = np.resize(x,(int(math.sqrt(x.size)),int(math.sqrt(x.size))))  
    y = np.resize(y,(int(math.sqrt(y.size)),int(math.sqrt(y.size))))   
    z = np.resize(z,(int(math.sqrt(z.size)),int(math.sqrt(z.size))))
    ax.plot_wireframe(x,y,z,color=colors[idx])
    patch = mlpat.Patch(color=colors[idx], label=keys[idx])
    legend.append(patch)

ax.set_ylabel("AVG Size(MB)")
ax.set_zlabel("AVG Load(%)")
ax.set_xlabel("AVG Performance(fps)")
ax.set_yticks(size_ticks,size_labels)
ax.set_zticks(load_ticks)
ax.set_xticks(perf_ticks,perf_labels)
plt.legend(handles=legend,loc='center right',bbox_to_anchor=(0.3, 0.8))
plt.subplots_adjust(left=0.0,bottom=0.0,top=1,right=1)

plt.show()
