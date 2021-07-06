# SCION-TV</br>
***This project enables TV-Webstreaming over the SCION-Network***</br>

*file_Server.go*  __->__  file-server with content-header to access HTTP-Livestream</br>
*server.go*  __->__  server which serves website and its resources</br>

*mov*  __->__  contains sample movie files and ffmpeg script to create HLS files</br> 
*hls*  __->__  contains playlist file and HLS video segments</br>

*html*  __->__  folder that contains website and its resources</br>
*html/index.html*  __->__  website uses Video JS as a Javascript based Videoplayer to consume HLS content</br>

The Website was created using this guide as a baseline:</br>
https://videojs.com/getting-started/
