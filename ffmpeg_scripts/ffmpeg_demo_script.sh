#!/bin/bash
cd ..
rm -rf hls/*.m3u8
rm -rf hls/*.mp4
rm -rf hls/*.m4s
cd hls
ffmpeg -i http://127.0.0.1:8890/bysid/772 -sn -vf scale=w=1280:h=720 -c:v:0 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:0 3M -maxrate:v:0 3M -minrate:v:0 3M -bufsize:v:0 9M -preset veryfast -g 48 -sc_threshold 0 -keyint_min 48 -c:a:0 aac -b:a:0 96k -ac 2 -f hls -hls_time 6 -hls_list_size 15 -hls_delete_threshold 5 -hls_flags independent_segments -hls_flags delete_segments -hls_flags split_by_time -hls_segment_type mpegts -hls_segment_filename "segment_%d.ts" "playlist.m3u8"
