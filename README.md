# SCION-TV</br>
***This project enables TV-Webstreaming over the SCION-Network***</br>
</br>

## Project-Overview:</br>

Folders:</br>
<i>[mov](mov) &nbsp; &nbsp; &nbsp;   </i>  <strong>-></strong>  contains sample movie files and a ffmpeg script to create corresponding HLS files         </br> 
<i>[hls_mov](hls_mov)</i>  <strong>-></strong>  contains playlist file and HLS video segments corresponding to a static movie file in mov </br>
<i>[hls](hls) &nbsp; &nbsp; &nbsp; &nbsp;    </i>  <strong>-></strong>  contains playlist file and HLS video segments corresponding to the main ffmpeg script     </br>
<i>[html](html) &nbsp; &nbsp;&nbsp;   </i>  <strong>-></strong>  contains website and its resources</br>

Website:</br>
<i>[index.html](html/index.html)</i>  <strong>-></strong>  website uses Video JS as a Javascript based Videoplayer to enable the consumption of HLS content </br>

Main Script:</br>
<i>[ffmpeg_script.sh](ffmpeg_script.sh)</i>  <strong>-></strong>  this script converts the video data stream into a true HLS. </br>

Servers:</br>
<i>[file_server.go](file_server.go) &nbsp;&nbsp;</i>  <strong>-></strong> file-server with content-header to access HTTP-Livestream files; runs with default setup on port 8899 </br>
<i>[web_server.go](web_server.go)&nbsp; </i>  <strong>-></strong> server which serves website and its resources; runs with default setup on port 80                     </br>
<i>[proxy](https://github.com/netsec-ethz/scion-apps/tree/master/_examples/shttp/proxy) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</i>  <strong>-></strong>  this server is part of the required SCION environment install; runs with recommended setup on port 8890 </br>

There exists a peer in the SCION-network which is broadcasting video content. In this specific case the video content is a TV-Signal. The video stream can be received through the SCION network. In order to watch the stream you need to be connected to the stream with the SCION proxy. The proxy will make the SCION-network content accessible to your own network or machine. This project uses ffmpeg to convert the data stream into a modern and easily accessible video streaming format and than re-distributes the content via the web and file servers in the LAN or on your own machine.  

## Project-Requirements:</br>
You will need a machine that runs Linux, is connected to the Internet and was configured to be a SCION-AS. [Here](https://www.scionlab.org/) you can learn more about SCION, the team behind it and how to become part of the network.</br>
Your machine's setup also has to include the required [GO](https://en.wikipedia.org/wiki/Go_(programming_language)) version installation and SCION proxy install from the [SCION-Apps Repository](https://github.com/netsec-ethz/scion-apps)</br>

## Recommended Script-Setup:</br>
<i>startFileServer.sh </i><pre>sudo \[PATH_to -> GO\] run \[PATH_to -> file_server.go\] \[PATH_to -> hls\]</pre>
<i>startWebServer.sh  </i><pre>sudo \[PATH_to -> GO\] run \[PATH_to -> web_server.go\] \[PATH_to -> html\]</pre>
<i>startProxyServer.sh</i><pre>sudo \[PATH_to -> proxy\] --remote="\[SCION-IP of Broadcast\]" --local="\[0.0.0.0:8890 or Device_LAN-IP:8890\]"</pre>
All of this scripts should be run automatically by crontab or a similar sheduling tool shortly after each other.</br>
Start up the proxy server first then start the file and web server afterwards since the later depend on the proxy server.</br>

## Used Rescources:</br>
The Website was created using this guide as a baseline:</br>
https://videojs.com/getting-started/
