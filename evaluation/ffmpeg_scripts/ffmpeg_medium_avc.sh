#!/bin/bash
cd ../..
rm -rf hls/*.m3u8
rm -rf hls/*.mp4
rm -rf hls/*.m4s
cd hls
ffmpeg -i http://127.0.0.1:8890/bysid/772 -sn -c:v:0 libx264 -preset medium -crf 20 -tune fastdecode -tune zerolatency -threads 4 -sc_threshold 0 -c:a:0 aac -b:a:0 96k -ac 2 -f hls -hls_time 6 -hls_list_size 15 -hls_flags single_file -hls_flags omit_endlist -hls_segment_type fmp4 -hls_fmp4_init_filename "init.mp4" -hls_segment_filename "segment_%d.mp4" "playlist.m3u8"
