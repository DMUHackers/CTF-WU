import os, sys
import Image

im = Image.open("code1.png")
pix = im.load()

number1 = ""
string = ""
for colour in range(1,12900,12):
	rgb1 = str(pix[1,colour][0]) + str(pix[1,colour][1]) + str(pix[1,colour][2])
	if rgb1 == "25500": shift = 0
	elif rgb1 == "1280128": shift = 1
	elif rgb1 == "00255": shift = 2
	elif rgb1 == "01280": shift = 3
	elif rgb1 == "2552550": shift = 4
	elif rgb1 == "2551650": shift = 5
	number2 = ""
	for num in range(85,169,12):
		rgb2 = str(pix[num,colour][0]) + str(pix[num,colour][1]) + str(pix[num,colour][2])
		if rgb2 == "000": number2 = number2 + "1"
		elif rgb2 == "255255255": number2 = number2 + "0"
	char = chr(int(number2,2)-shift)
	string = string + char
print string
