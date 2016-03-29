'''
	ffmpeg-seriesedit

	Simple example of how to create to cuts in a series of operations (one edit, followed by a second edit)

	Christopher Konopka 2016
'''

import os
import time
import sys

# delete previously edited files for the demonstration
if os.path.isfile("vidA.mp4") == True and os.path.isfile("vidB.mp4") == True:
	os.remove('vidA.mp4')
	os.remove('vidB.mp4')
else:
	print ('continue')	

# main video
video = '../videos/vid1.mp4'

# edit #1
time.sleep(.1)
os.system("ffmpeg -i %s -ss 00:00:00 -to 00:00:03 -c copy vidA.mp4" % video)

# edit #2
time.sleep(.1)
os.system("ffmpeg -i %s -ss 00:00:09 -to 00:00:12 -c copy vidB.mp4" % video)
