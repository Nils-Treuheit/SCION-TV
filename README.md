# SCION-TV</br>
***This project enables TV-Webstreaming over the SCION-Network***</br>
</br>

Servers:</br>
<i>'file_Server.go'</i>  <strong>-></strong>  file-server with content-header to access HTTP-Livestream</br>
<i>'server.go'</i>       <strong>-></strong>  server which serves website and its resources</br>

Folders:</br>
<i>'mov'</i>  <strong>-></strong>  contain sample movie files and ffmpeg script to create HLS files</br> 
<i>'hls'</i>  <strong>-></strong>  contain playlist file and HLS video segments</br>
<i>'html'</i> <strong>-></strong>  contain website and its resources</br>

Website:</br>
<i>'html/index.html'</i> <strong>-></strong> website uses Video JS as a Javascript based Videoplayer to consume HLS content</br>
</br>

The Website was created using this guide as a baseline:</br>
https://videojs.com/getting-started/
