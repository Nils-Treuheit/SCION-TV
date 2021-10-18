cd ../../
rm -rf hls/*
cd hls
ffmpeg -i http://127.0.0.1:8890/bysid/772 -sn -c:v:0 libaom-av1 -crf 35 -b:v:0 0 -c:a:0 aac -b:a:0 96k -ac 2 -f hls -hls_time 6 -hls_list_size 15 -hls_flags single_file -hls_flags omit_endlist -hls_segment_type fmp4 -hls_fmp4_init_filename "init.mp4" -hls_segment_filename "segment_%d.mp4" "playlist.m3u8"
