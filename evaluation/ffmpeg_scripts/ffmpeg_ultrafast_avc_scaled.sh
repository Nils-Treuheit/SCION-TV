cd ../..
rm -rf hls/*.m3u8
rm -rf hls/*.mp4
rm -rf hls/*.m4s
cd hls
ffmpeg -i http://127.0.0.1:8890/bysid/772 -sn -vf scale=w=1280:h=720 -c:v:0 libx264 -preset ultrafast -crf 23 -tune fastdecode -tune zerolatency -c:a:0 aac -b:a:0 96k -ac 2 -f hls -hls_time 6 -hls_list_size 15 -hls_flags delete_segments -hls_flags omit_endlist -hls_segment_type fmp4 -hls_fmp4_init_filename "init.mp4" -hls_segment_filename "segment_%d.m4s" "playlist.m3u8"
