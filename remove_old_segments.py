import os, time
while True:
	os.system('find ./hls -name "segment_*.m4s" -mmin +5 -type f -exec rm -fv {} \;')
	time.sleep(150)
