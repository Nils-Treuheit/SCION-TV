import os, sys, time

if (sys.argv>1):
	fname = sys.argv[1]
	os.system(('cd ./hls && ls -la > '+fname))
	while True:
                os.system('find ./hls -name "segment_*.m4s" -mmin +5 -type f -exec rm -fv {} \;')
                time.sleep(90)
		os.system(('cd ./hls && ls -la >> '+fname))
else:
	while True:
		os.system('find ./hls -name "segment_*.m4s" -mmin +5 -type f -exec rm -fv {} \;')
		time.sleep(90)
