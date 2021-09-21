# SCION-TV</br>
***This project enables TV-Webstreaming over the SCION-Network***</br>
</br>

## Project-Overview:</br>

Folders:</br>
<i>[mov](mov)</i>           <strong>-></strong>  contains sample movie files and a ffmpeg script to create corresponding HLS files</br> 
<i>[hls_mov](hls_mov)</i>   <strong>-></strong>  contains playlist file and HLS video segments corresponding to a static movie file in mov</br>
<i>[hls](hls)</i>           <strong>-></strong>  contains playlist file and HLS video segments corresponding to the main ffmpeg script</br>
<i>[html](html)</i>         <strong>-></strong>  contains website and its resources</br>

Website:</br>
<i>[index.html](html/index.html)</i> <strong>-></strong> website uses Video JS as a Javascript based Videoplayer to enable the consumption of HLS content</br>

Main Script:</br>
<i>[ffmpeg_script.sh](ffmpeg_script.sh)</i> <strong>-></strong> this script converts the video data stream into a true HLS.</br>

Servers:</br>
<i>[file_server.go](file_server.go)</i>  <strong>-></strong>  file-server with content-header to access HTTP-Livestream files</br>
<i>[web_server.go](web_server.go)</i>    <strong>-></strong>  server which serves website and its resources</br>
<i>[proxy](https://github.com/netsec-ethz/scion-apps/tree/master/_examples/shttp/proxy)</i>  <strong>-></strong>  this server is part of the required SCION environment install</br>

There exists a peer in the SCION-network which is broadcasting video content. In this specific case the video content is a TV-Signal. The video stream can be received through the SCION network. In order to watch the stream you need to be connected to the stream with the SCION proxy. The proxy will make the SCION-network content accessible to your own network or machine. This project uses ffmpeg to convert the data stream into a modern and easily accessible video streaming format and than re-distributes the content via the web and file servers in the LAN or on your own machine.  

## Project-Requirements:</br>
You will need a machine that runs Linux, is connected to the Internet and was configured to be a SCION-AS. [Here](https://www.scionlab.org/) you can learn more about SCION, the team behind it and how to become part of the network.</br>
Your machine's setup also has to include the required [GO](https://en.wikipedia.org/wiki/Go_(programming_language)) version installation and SCION proxy install from the [SCION-Apps Repository](https://github.com/netsec-ethz/scion-apps)</br>

## Used Rescources:</br>
The Website was created using this guide as a baseline:</br>
https://videojs.com/getting-started/
