# SCION-TV</br>
***This project enables TV-Webstreaming over the SCION-Network***</br>

file_Server.go -> file-server with content-header to access HTTP-Livestream</br>
server.go -> server which serves website and its resources</br>

mov -> contains sample movie files and ffmpeg script to create HLS files</br> 
hls -> contains playlist file and HLS video segments</br>

html -> folder that contains website and its resources</br>
html/index.html -> website uses Video JS as a Javascript based Videoplayer to consume HLS content</br>

The Website was created using this guide as a baseline:</br>
https://videojs.com/getting-started/
