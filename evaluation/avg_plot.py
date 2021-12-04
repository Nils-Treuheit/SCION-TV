from glob import glob
import math, numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mlpat
from mpl_toolkits.mplot3d import Axes3D

files = glob("data/avg_*.gen_log")

keys,active_loads,loads,perfs,sizes = ([],[],[],[],[])
for filename in files:
    enc_format = (filename.split(".")[0].split("_")[-1])
    file = open(filename,"r")
    lines = file.readlines()
    for line_count,line in enumerate(lines):
        if line_count%5==0: 
            keys.append((enc_format + "_" +line.strip()))
        elif line_count%5==1:
            perfs.append(float(line.split(" ")[1]))
        elif line_count%5==2:     
            active_loads.append(float(line.split(" ")[1]))
        elif line_count%5==3:     
            loads.append(float(line.split(" ")[1]))
        elif line_count%5==4:     
            sizes.append(float(line.split(" ")[1]))
    file.close()

avg_load = (sum(loads)+sum(active_loads))/(len(loads)+len(active_loads))
avg_size = sum(sizes)/len(sizes)
avg_perf = sum(perfs)/len(perfs)
load_ticks = [*range(0,101,10)]
size_ticks = [0,1,*range(5,math.ceil(max(sizes)+2),10)]
size_labels = [0,"",*range(5,math.ceil(max(sizes)+2),10)]
perf_ticks = sorted([*range(0,71,10),55,45,75])
perf_labels = [*range(0,50,10),"",50,"",60,"",75]
colors = ["tab:blue","tab:cyan","tab:red","tab:orange","tab:green","tab:olive","tab:purple","tab:pink","tab:brown","tab:grey"]
#cmaps = ["Blues","cool","Reds","Oranges","Greens","summer","Purples","spring","copper","Greys"]

plt.figure(0)
legend = []
plt.scatter(avg_load,avg_size,c='k',alpha=0.2)
for idx in range(len(keys)):
    x1 = np.zeros(len(size_ticks))+loads[idx]
    x2 = np.zeros(len(size_ticks))+active_loads[idx]
    y = np.zeros(len(load_ticks))+sizes[idx]
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

plt.figure(1)
legend = []
plt.scatter(avg_load,avg_perf,c='k',alpha=0.2)
for idx in range(len(keys)):
    x1 = np.zeros(len(perf_ticks))+loads[idx]
    x2 = np.zeros(len(perf_ticks))+active_loads[idx]
    y = np.zeros(len(load_ticks))+perfs[idx]
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

plt.figure(2)
legend = []
plt.scatter(avg_perf,avg_size,c='k',alpha=0.2)
for idx in range(len(keys)):
    x = np.zeros(len(size_ticks))+perfs[idx]
    y = np.zeros(len(perf_ticks))+sizes[idx]
    plt.plot(x,size_ticks,"-",color=colors[idx])
    plt.plot(perf_ticks,y,"-",color=colors[idx])
    patch = mlpat.Patch(color=colors[idx], label=keys[idx])
    legend.append(patch)
plt.ylabel("AVG Size(MB)")
plt.xlabel("AVG Perforance(fps)")
plt.yticks(size_ticks,size_labels)
plt.xticks(perf_ticks,perf_labels)
plt.legend(handles=legend)

fig = plt.figure(3)
ax = plt.axes(projection='3d')
legend = []
for idx in range(len(keys)):
    x,y,z = (np.arange(perfs[idx]-perfs[idx]/8,perfs[idx]+perfs[idx]/8,((perfs[idx]+perfs[idx]/8)-(perfs[idx]-perfs[idx]/8))/20),
             np.arange(sizes[idx]-sizes[idx]/8,sizes[idx]+sizes[idx]/8,((sizes[idx]+sizes[idx]/8)-(sizes[idx]-sizes[idx]/8))/20),
             np.arange(loads[idx],active_loads[idx]*2-loads[idx],(active_loads[idx]*2-loads[idx]*2)/20))
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
ax.set_xlabel("AVG Perforance(fps)")
ax.set_yticks(size_ticks,size_labels)
ax.set_zticks(load_ticks)
ax.set_xticks(perf_ticks,perf_labels)
plt.legend(handles=legend)

plt.show()
