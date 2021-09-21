# SCION-TV</br>
***This project enables TV-Webstreaming over the SCION-Network***</br>
</br>

Servers:</br>
<i>[file_server.go](file_server.go)</i>  <strong>-></strong>  file-server with content-header to access HTTP-Livestream files</br>
<i>[web_server.go](web_server.go)</i>    <strong>-></strong>  server which serves website and its resources</br>

Folders:</br>
<i>[mov](mov)</i>           <strong>-></strong>  contains sample movie files and a ffmpeg script to create corresponding HLS files</br> 
<i>[hls_mov](hls_mov)</i>   <strong>-></strong>  contains playlist file and HLS video segments corresponding to a static movie file in mov</br>
<i>[hls](hls)</i>           <strong>-></strong>  contains playlist file and HLS video segments corresponding to the main ffmpeg script</br>
<i>[html](html)</i>         <strong>-></strong>  contains website and its resources</br>

Website:</br>
<i>[index.html](html/index.html)</i> <strong>-></strong> website uses Video JS as a Javascript based Videoplayer to enable the consumption of HLS content</br>
</br>

The Website was created using this guide as a baseline:</br>
https://videojs.com/getting-started/
