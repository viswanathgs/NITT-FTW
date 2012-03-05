#!/usr/bin/python -tt

##
# This script casts votes for NITT at the IndiaToday poll.
#
# Usage: python nittftw.py <number_of_votex>
#					or
#		sudo chmod u+x nittftw.py
#		./nittftw.py <number_of_votes>
#
##

import sys
import Image
import mechanize
import md5
import random
import string

def cast_votes():
	if (len(sys.argv) != 2):
		print 'Syntax: python nittftw.py <number_of_votes>'
		exit(-1)

	votes = int(sys.argv[1])
	success = 0
	for vote in range(votes):
		print 'Iteration ' + str(vote + 1) + ': '

		br = mechanize.Browser()
		br.open('http://specials.indiatoday.com/survey/bestcollegespoll2011/engineering.jsp')
		br.select_form('englist')
	
		br.form['name'] = 'shadynittian'
		br.form['email'] = ''.join(random.choice(string.ascii_lowercase) for x in range(random.randrange(1,20))) + '@nittian.com'
		br.form['mobile'] = '1337'
		br.form['artcolege'] = ['National Institute of Technology, Tiruchirapally']

		br.retrieve('http://specials.indiatoday.com/survey/bestcollegespoll2011/img.jsp', 'img.png')
		captcha = extract_captcha('img.png')

		success_flag = False

		if (captcha != ''):
			print 'captcha = ' + captcha
			br.form['number'] = captcha
			response = br.submit()
			if (br.geturl() == 'http://specials.indiatoday.com/survey/bestcollegespoll2011/colleges_results.jsp?survey_id=1010117'):
				success_flag = True					

		if success_flag:	
			print 'Success :)'
			success += 1
		else:
			print 'Failed :('

	print 'Congratulations! You have cast ' + str(success) + ' vote(s) for NITT. \m/'

def extract_captcha(image_file):
	captcha = ''
	im = Image.open(image_file)

	start = False
	startx = 0

	for x in range(75):
		white = True
		for y in range(35):
			if (im.getpixel((x,y)) == (0,0,0)):
				white = False
				break
		if (white and start):
			start = False
			text = extract_char(im.crop((startx,0,x,34)))
			if (text == ''):
				return ''
			captcha += text
		elif ((not white) and (not start)):
			start = True
			startx = x-1	

	return captcha

def extract_char(im):
	all_text = '0123456789abcdef'
	
	for i in range(len(all_text)):
		im2 = Image.open('captcha/' + all_text[i] + '.png')
		if (im.tostring() == im2.tostring()):
			return all_text[i]

	return ''

if __name__ == '__main__':
	cast_votes()
