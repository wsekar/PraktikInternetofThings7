from time import *
from gpio import *
from ioeclient import *
from physical import * #import modul physical

def onInputReceive(input): #Fungsi onInputReceive() dengan parameter input 
	if input == "0": #jika input merupakan value "0" maka
		print("going up") #mobil akan bergerak ke atas
		moveBy(0, -20) #fungsi moveBy dengan parameter digunakan untuk mengontrol posisi atau gerak mobil
	elif input == "1": #jika input merupakan value "1" maka
		print("going down") #mobil akan bergerak ke bawah
		moveBy(0, 20);
	elif input == "2": #jika input merupakan value "2" maka
		print("going left") #mobil akan bergerak ke kiri
		moveBy(-20, 0); 
	elif input == "3": #jika input merupakan value "3" maka
		print("going right") #mobil akan bergerak ke kanan
		moveBy(20, 0);
	else:
		print("stop") #mobil berhenti

		

def main():
	# Setup Registration Server	
	IoEClient.setup({
		"type": "Car",
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
			"controllable": True
		}]
	});

	IoEClient.onInputReceive(onInputReceive)

	while True:
		delay(500)

if __name__ == "__main__":
	main()
