# SCION-TV</br>
***This project enables TV-Webstreaming over the SCION-Network***</br>
</br>

## Project-Overview:</br>

Folders:</br>
<i>[mov](mov) &nbsp; &nbsp; &nbsp;   </i>  <strong>-></strong>  contains sample movie files and a [ffmpeg](https://ffmpeg.org/ffmpeg-formats.html#hls-2) script to create corresponding HLS files         </br> 
<i>[hls_mov](hls_mov)</i>  <strong>-></strong>  contains playlist file and HLS video segments corresponding to a static movie file in mov </br>
<i>[hls](hls) &nbsp; &nbsp; &nbsp; &nbsp;    </i>  <strong>-></strong>  contains playlist file and HLS video segments corresponding to the main ffmpeg script     </br>
<i>[html](html) &nbsp; &nbsp;&nbsp;   </i>  <strong>-></strong>  contains website and its resources</br>

Helper Scripts:</br>
<i>[remove_old_segments.py](remove_old_segments.py)   </i>  <strong>-></strong> time based maintainace script to remove segment files that will not be used anymore </br>
<i>[webpage_generator.py](webpage_generator.py) &nbsp; &nbsp;   </i>  <strong>-></strong> build script to modify the website file according to network setup </br>

Website:</br>
<i>[index.html](html/index.html)</i>  <strong>-></strong>  website uses [Video JS](https://videojs.com/) as a Javascript based Videoplayer to enable the consumption of HLS content </br>

Main Script:</br>
<i>[ffmpeg_ultrafast_avc.sh](ffmpeg_scripts/avc/ffmpeg_ultrafast_avc.sh)</i>  <strong>-></strong>  mainly used script in the project that converts the video data stream into a true HLS. </br>
<i>[ffmpeg_scripts](ffmpeg_scripts)</i>  <strong>-></strong>  this folder contains different scripts that can convert the video data stream into a true HLS. </br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;  &nbsp;  &nbsp;</i>  <strong>-></strong> the folder is split into subfolders that hold scripts for the respective encoding formats </br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;  &nbsp;  &nbsp;</i>  <strong>-></strong> each subfolder holds 3 scripts </br>

The idea behind this setup is to provide 3 basic levels of encoding performance through these scripts. You can choose the base script depending on your machines performance and then tweak it to fit even better to your machine's transcoding power. The naming hints on the needed system performance => ultrafast & realtime scripts are the least demanding, veryslow & best are the most demanding. There are scripts ready for encoding with the following standards: [avc](ffmpeg_scripts/avc), [hevc](ffmpeg_scripts/hecv), [vp9](ffmpeg_scripts/vp9) and [av1](ffmpeg_scripts/av1). </br></br>


Servers:</br>
<i>[file_server.go](file_server.go) &nbsp;&nbsp;</i>  <strong>-></strong> file-server with content-header to access HTTP-Livestream files</br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;   &nbsp;   &nbsp;&nbsp;</i>  <strong>-></strong> runs with default setup on port 8899 </br>
<i>[web_server.go](web_server.go)&nbsp; </i>  <strong>-></strong> server which serves website and its resources </br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;   &nbsp;   &nbsp;&nbsp;</i>  <strong>-></strong> runs with default setup on port 80                     
<i>[proxy](https://github.com/netsec-ethz/scion-apps/tree/master/_examples/shttp/proxy) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</i>  <strong>-></strong>  this server is part of the required [SCION](https://scion-architecture.net) environment install</br>
<i>  &nbsp;  &nbsp;  &nbsp;  &ensp;  &nbsp;  &nbsp;  &ensp;  &ensp;   &nbsp;   &nbsp;&nbsp;</i>  <strong>-></strong> runs with recommended setup on port 8890 </br>

There exists a peer in the SCION-network which is broadcasting video content. In this specific case the video content is a TV-Signal. The video stream can be received through the SCION network. In order to watch the stream you need to be connected to the stream with the SCION proxy. The proxy will make the SCION-network content accessible to your own network or machine. This project uses ffmpeg to convert the data stream into a modern and easily accessible video streaming format and than re-distributes the content via the web and file servers in the LAN or on your own machine.  

## Project-Requirements:</br>
You will need a machine that runs Linux, is connected to the Internet and was configured to be a SCION-AS. [Here](https://www.scionlab.org/) you can learn more about SCION, the team behind it and how to become part of the network.</br>
Your machine's setup also has to include the required [GO](https://golang.org/dl/#go1.16) version installation and SCION proxy install from the [SCION-Apps Repository](https://github.com/netsec-ethz/scion-apps).</br>

## Recommended Start-Up Script Setup:</br>
<i>startFileServer.sh </i><pre>sudo \[PATH_to -> GO\] run \[PATH_to -> file_server.go\] \[PATH_to -> hls\]</pre>
<i>startWebServer.sh  </i><pre>sudo \[PATH_to -> GO\] run \[PATH_to -> web_server.go\] \[PATH_to -> html\]</pre>
<i>startProxyServer.sh</i><pre>sudo \[PATH_to -> proxy\] --remote="\[SCION-IP of Broadcast\]" --local="\[0.0.0.0:8890 or Device_LAN-IP:8890\]"</pre>
</br>All of this scripts should be run automatically simultaneously with a script like this:</br></br>
<i>startServers.sh</i><pre>trap 'kill $BPID1; kill $BPID2;exit' EXIT
sudo ./startWebServer.sh & BPID1=$! sudo ./startFileServer.sh & BPID2=$! sudo ./startProxy.sh</pre>
Feel free to run that script shortly after the start-up by crontab or a similar sheduling tool.</br>
Just make sure that the Servers are started before the ffmpeg script, because of the dependency.</br>

## Used Rescources:</br>
The Website uses a picture creation made from these two pictures: [Picture 1](https://www.theatlantic.com/science/archive/2021/03/black-hole-cygnus-suprise/618049/), [Picture 2](https://www.flaticon.com/de/kostenloses-icon/wiedergabetaste_375?term=play%20taste&page=1&position=2&page=1&position=2&related_id=375&origin=tag)</br>
The Website was created using [this guide](https://videojs.com/getting-started/) from Video JS as a baseline.</br>
At the moment Video JS sadly only properly supports one of our encoding formats, which is [advanced video coding(avc)](https://en.wikipedia.org/wiki/Advanced_Video_Coding) or better known as H.264. An overview of supported encoding and stream formats can be found [here](https://github.com/videojs/http-streaming/blob/main/docs/supported-features.md).</br>

## Future Upgrade:</br>
Use [Google's Shakaplayer](https://opensource.google/projects/shaka-player) insetead of Video JS. The player from Google should support more encoding formats and should be more efficent since it is a local setup. However, this player requires an [extensive setup](https://shaka-player-demo.appspot.com/docs/api/tutorial-welcome.html) of an additional server infrastructure.    
