from usb import * #import modul usb
from time import * #import modul time
from gpio import * #import modul gpio
from ioeclient import * #import modul ioeclient

def getDir(x): #membuat arah atau posisi gerak
	if "up" in x: 
		print("up") #move up
		return "0" #mengembalikan nilai 0 sebagai option up pada IoEClient.setup
	elif "down" in x:
		print("down") #move down
		return "1" #mengembalikan nilai 1 sebagai option down pada IoEClient.setup
	elif "left" in x:
		print("left") #move left
		return "2" #mengembalikan nilai 2 sebagai option left pada IoEClient.setup
	elif "right" in x:
		print("right") #move right
		return "3" #mengembalikan nilai 3 sebagai option right pada IoEClient.setup
	else:
		print(x)
		return "4" #mengembalikan nilai 4 sebagai option stop pada IoEClient.setup

def main():
	# start USB
	usb = USB(0, 57600)

	# Setup Registration Server	
	IoEClient.setup({
		"type": "SBC",
		"states": [{
			"name": "Direction",
			"type": "options",
			"options": {
				"0" : "Up",
				"1" : "Down",
				"2" : "Left",
				"3" : "Right",
				"4" : "Stop"
			},
			"controllable": False
		}]
	});

	while True:
		# read from USB
		direction=""
		while usb.inWaiting() > 0:
			direction = usb.readLine() #membaca arah atau posisi gerak dengan fungsi usb.readLine()
			IoEClient.reportStates(getDir(direction)) 
		delay(500)

if __name__ == "__main__":
	main()
