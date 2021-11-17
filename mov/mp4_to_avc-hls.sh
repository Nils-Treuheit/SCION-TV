#!/bin/bash
ffmpeg -i sample.mp4 -vf scale=w=1280:h=720 -c:v:0 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:0 5M -maxrate:v:0 5M -minrate:v:0 5M -bufsize:v:0 25M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 -c:a:0 aac -b:a:0 96k -ac 2 -f hls -hls_time 15 -hls_playlist_type vod -hls_segment_type mpegts -hls_segment_filename "../hls_vod/segment_%d.ts" "../hls_vod/playlist.m3u8"
