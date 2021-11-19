# SCION-TV</br>
***This project enables TV-Webstreaming over the SCION-Network***</br>
</br>

## Project-Overview:</br>

Folders:</br>
---------</br>
<i>[evaluation](evaluation) </i>  <strong>-></strong>  contains the [scripts](evaluation/scripts) that are used for evaluation and the [data](evaluation/data) that was collected</br>
<i>[mov](mov) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  </i>  <strong>-></strong>  contains sample movie files and a [ffmpeg](https://ffmpeg.org/ffmpeg-formats.html#hls-2) script to create corresponding HLS files         </br> 
<i>[hls_mov](hls_mov) &nbsp;&nbsp;&nbsp; </i>  <strong>-></strong>  contains playlist file and HLS video segments corresponding to a static movie file in mov </br>
<i>[hls](hls) &nbsp;&nbsp;  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;  </i>  <strong>-></strong>  contains playlist file and HLS video segments corresponding to the main ffmpeg script     </br>
<i>[html](html) &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;  </i>  <strong>-></strong>  contains website and its resources</br></br>


Helper Scripts:</br>
----------------</br>
<i>[remove_old_segments.py](remove_old_segments.py)   </i>  <strong>-></strong> time based maintainace script to remove segment files that will not be used anymore </br>
<i>[webpage_generator.py](webpage_generator.py) &nbsp; &nbsp;   </i>  <strong>-></strong> build script to modify the website file according to network setup </br>
<i>remove_old_segments.py & [perf.sh](evaluation/perf.sh)</i>  <strong>-></strong> are used for collecting evaluation data</br></br>


Website:</br>
----------</br>
<i>[index.html](html/index.html)</i>  <strong>-></strong>  website uses [Video JS](https://videojs.com/) as a Javascript based Videoplayer to enable the consumption of HLS content </br></br>


Main Script:</br>
-------------</br>
<i>[ffmpeg_ultrafast_avc.sh](ffmpeg_scripts/avc/ffmpeg_ultrafast_avc.sh)</i>  <strong>-></strong>  mainly used script in the project that converts the video data stream into a true HLS. </br>
<i>[ffmpeg_scripts](ffmpeg_scripts)</i>  <strong>-></strong>  this folder contains different scripts that can convert the video data stream into a true HLS. </br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;  &nbsp;  &nbsp;&nbsp;</i>  <strong>-></strong> the folder is split into subfolders that hold scripts for the respective encoding formats </br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;  &nbsp;  &nbsp;&nbsp;</i>  <strong>-></strong> each subfolder holds 3 scripts </br>

The idea behind this setup is to provide 3 basic levels of encoding performance through these scripts. You can choose the base script depending on your machines performance and then tweak it to fit even better to your machine's transcoding power. The naming hints on the needed system performance => ultrafast & realtime scripts are the least demanding, veryslow & best are the most demanding. There are scripts ready for encoding with the following standards: [avc](ffmpeg_scripts/avc), [hevc](ffmpeg_scripts/hecv), [vp9](ffmpeg_scripts/vp9) and [av1](ffmpeg_scripts/av1). </br></br>


Server Setup:</br>
---------------</br>
<i>[server.go](server.go)</i> contains the entire server setup and is implemented in Go </br></br>
The setup includes the following components:</br>
<i>[file server](https://github.com/Nils-Treuheit/SCION-TV/blob/0b8c8f0ffc8613eb76f95da0c6d5a88a987b188d/file_server.go) &nbsp;</i>  <strong>-></strong> file-server with content-header to access HTTP-Livestream files</br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;</i>  <strong>-></strong> runs with default setup on port 8899 </br>
<i>[web server](https://github.com/Nils-Treuheit/SCION-TV/blob/0b8c8f0ffc8613eb76f95da0c6d5a88a987b188d/web_server.go)&nbsp; </i>  <strong>-></strong> server which serves website and its resources </br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;</i>  <strong>-></strong> runs with default setup on port 8080                    
<i>[proxy](https://github.com/netsec-ethz/scion-apps/tree/master/_examples/shttp/proxy) &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</i>  <strong>-></strong>  this server is part of the required [SCION](https://scion-architecture.net) environment install</br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;</i>  <strong>-></strong> runs with recommended setup on port 8890 </br>

There exists a peer in the SCION-network which is broadcasting video content. In this specific case the video content is a TV-Signal. The video stream can be received through the SCION network. In order to watch the stream you need to be connected to the stream with the SCION proxy. The proxy will make the SCION-network content accessible to your own network or machine. This project uses ffmpeg to convert the data stream into a modern and easily accessible video streaming format and than re-distributes the content via the web and file servers in the LAN or on your own machine.  
</br>


## Recommended Script Setup:</br>
<i>startServerSetup.sh </i>
```shell-script 
[PATH_to -> GO] run [PATH_to -> server.go]
```
This script will execute the server.go program with default values for all its parameters.</br>
Feel free to run that script shortly after the start-up by crontab or a similar sheduling tool.</br>
Just make sure that the Servers are started before the ffmpeg script, because of the dependency.</br>
You can run the server.go program with your own values for all its parameters.</br>
This is how the command would look like with all optional paramters:
```shell
[PATH_to -> GO] run [PATH_to -> server.go] --webServPort="[PORT of Webpage]" --webDir="[Directory of HTML-File]" \
                                           --fileServPort="[PORT of File Server]" --fileDir="[Directory of HLS content]" \
                                           --remote="[SCION-IP of Broadcast]" --local="[0.0.0.0:8890 or Device_LAN-IP:8890]"
```
Besides the server.go program you should simultaneously run the remove_old_segments.py and a ffmpeg script that transcodes the MuMuDVB-Stream to a HTTP-Livestream.  
</br>

## Project-Requirements:</br>
You will need a machine that runs Linux, is connected to the Internet and was configured to be a SCION-AS. [Here](https://www.scionlab.org/) you can learn more about SCION, the team behind it and how to become part of the network.</br>
Your machine's setup also has to include the required [GO](https://golang.org/dl/#go1.16) version installation and [SCION apps](https://github.com/netsec-ethz/scion-apps) installation. Please refer to the installation guide of the SCION apps repository.</br>
If you want to follow my exact setup you will need to install VirtualBox, Vagrant and get the Vagrantfile from your SCION-AS configuartion. You definitely have to add some lines to your Vagrantfile regarding port forwarding. If you choose to use the default configuration you need to add these lines in the Vagrantfile:
<pre>config.vm.network "forwarded_port", guest: 8080, host: 80, protocol: "tcp"
config.vm.network "forwarded_port", guest: 8890, host: 8890, protocol: "tcp"
config.vm.network "forwarded_port", guest: 8899, host: 8899, protocol: "tcp"</pre>
In my setup I used a Ubuntu Bionic(18.04) 64-bit VM with the following SCION apps installation:
```shell
sudo apt-get install apt-transport-https
echo "deb [trusted=yes] https://packages.netsec.inf.ethz.ch/debian all main" | sudo tee /etc/apt/sources.list.d/scionlab.list
sudo apt-get update
sudo apt install scion-apps-*
```
and the following Go(version 1.16) installation:
```shell
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt update
sudo apt install golang-1.16
```
If you mirrored my setup you will find your go application under <code>/usr/lib/go-1.16/bin</code>
</br></br>

## Used Rescources:</br>
The Website uses a picture creation made from these two pictures: [Picture 1](https://www.theatlantic.com/science/archive/2021/03/black-hole-cygnus-suprise/618049/), [Picture 2](https://www.flaticon.com/de/kostenloses-icon/wiedergabetaste_375?term=play%20taste&page=1&position=2&page=1&position=2&related_id=375&origin=tag)</br>
The Website was created using [this guide](https://videojs.com/getting-started/) from Video JS as a baseline.</br>
At the moment Video JS sadly only properly supports one of our encoding formats, which is [advanced video coding(avc)](https://en.wikipedia.org/wiki/Advanced_Video_Coding) or better known as H.264. An overview of supported encoding and stream formats can be found [here](https://github.com/videojs/http-streaming/blob/main/docs/supported-features.md).</br></br>

## Future Upgrade:</br>
Use [Google's Shakaplayer](https://opensource.google/projects/shaka-player) insetead of Video JS. The player from Google should support more encoding formats and should be more efficent since it is a local setup. However, this player requires an [extensive setup](https://shaka-player-demo.appspot.com/docs/api/tutorial-welcome.html) of an additional server infrastructure.    
