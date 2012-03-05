#!/usr/bin/python -tt

##
# Helper for extracting captcha files and splitting into
# individual pieces of characters
#
##

import urllib
import Image

urllib.urlretrieve('http://specials.indiatoday.com/survey/bestcollegespoll2011/img.jsp', 'captcha/img.png')
im = Image.open('captcha/img.png')

count = 1
start = False
startx = 0

for x in range(75):
	white = True
	for y in range(35):
		if (im.getpixel((x,y)) == (0, 0, 0)):
			white = False
			break
	if (white and start):
		start = False
		im.crop((startx,0,x,34)).save('captcha/f'+str(count),'PNG')
		count += 1
	elif ((not white) and (not start)):
		start = True
		startx = x-1
