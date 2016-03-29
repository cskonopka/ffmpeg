'''
	ffmpeg-cutandconcat

	Simple example of how to cut a section of a video using ffmpeg.

	Christopher Konopka 2016
'''

import os
import time
import sys

video1 = '../videos/vid1.mp4'
video2 = '../videos/vid2.mp4'

if os.path.isfile("glued.mp4") == True:
	os.remove('glued.mp4')
else:
	print ('continue')	

# create a new file to add each cut to the list
file = open("videolist.txt", "w")

# cut #1
time.sleep(.1)
os.system("ffmpeg -i %s -ss 00:00:00 -to 00:00:03 -c copy vidA.mp4" % video1)
# add new cut #1 to list
file.write("file 'vidA.mp4'\r")

# cut #2
time.sleep(.1)
os.system("ffmpeg -i %s -ss 00:00:09 -to 00:00:12 -c copy vidB.mp4" % video2)
# add new cut #2 to list
file.write("file 'vidB.mp4'")

# close file containing a list of the 2 new edits
time.sleep(.1)
file.close()

# concatenate the videos which were added to the newly created file
time.sleep(.1)
# create new "concatvideo"
os.system("ffmpeg -f concat -i videolist.txt -codec copy concatvideo.mp4")
# clean up cut videos to save space
os.remove('vidA.mp4')
os.remove('vidB.mp4')
time.sleep(.1)