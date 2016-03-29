'''
	ffmpeg-cut

	Simple example of how to cut a section of a video using ffmpeg.

	Christopher Konopka 2016
'''

import os
import time
import sys

time.sleep(.5)

os.system("ffmpeg -i vid1.mp4 -ss 00:00:00 -to 00:00:05 -c copy vidA.mp4")