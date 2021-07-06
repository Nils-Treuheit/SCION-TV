# SCION-TV
TV-Webstreaming over the SCION-Network

file_Server.go -> file-server with content-header to access HTTP-Livestream 
server.go -> server which serves website and its resources 

hls -> contains playlist file and HLS video segments
html -> folder that contains website and its resources
html/index.html -> website uses Video JS as a Javascript based Videoplayer to consume HLS content
