'''
	ffmpeg-cut

	Simple example of how to cut a section of a video using ffmpeg.

	Christopher Konopka 2016
'''

import os
import time
import sys

# video content
video = '../videos/vid1.mp4'

# cut video
os.system("ffmpeg -i %s -ss 00:00:00 -to 00:00:05 -c copy vidA.mp4" % video)