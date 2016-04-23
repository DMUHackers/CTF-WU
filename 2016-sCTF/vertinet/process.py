import sys, socket, struct, time, base64, os, Image, time
s = socket.socket()
host = 'problems1.2016q1.sctf.io'
port = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
x = 0
while True:
	data = s.recv(100000).split("'")
	print data
	x += 1
	image = data[1].replace("data:image/png;base64,","")
	imgdata = base64.b64decode(image)
	filename = 'code' + str(x) + '.png'
	with open(filename, 'wb') as f:
		f.write(imgdata)
	im = Image.open("code" + str(x) + ".png")
	pix = im.load()
	number1 = ""
	string = ""
	for colour in range(1,360,12):
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
	s.send(string)
	print string
	time.sleep(0.5)
