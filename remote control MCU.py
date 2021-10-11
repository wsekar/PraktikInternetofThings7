from usb import * #import modul usb
from time import * #import modul time
from gpio import * #import modul gpio

def main():
	# start USB
	usb = USB(0, 57600)
	pinMode(0, IN) #pin 0 sebagai input
	pinMode(1, IN) #pin 1 sebagai input
	pinMode(2, IN) #pin 2 sebagai input
	pinMode(3, IN) #pin 3 sebagai input
	while True:
        #digitalRead untuk membaca input dari pin
		if digitalRead(0) == HIGH: #digitalRead mendapatkan sinyal dari D0. Jika button Left ditekan maka button akan mengirimkan sinyal D0 dengan value HIGH
			usb.write("left"); #MCU akan mengirim value ke USB dengan menggunakan fungsi usb.write()
		elif digitalRead(1) == HIGH: #digitalRead mendapatkan sinyal dari D1. Jika button Right ditekan maka button akan mengirimkan sinyal D1 dengan value HIGH
			usb.write("right"); #MCU akan mengirim value ke USB dengan menggunakan fungsi usb.write()
		elif digitalRead(2) == HIGH: #digitalRead mendapatkan sinyal dari D2. Jika button Up ditekan maka button akan mengirimkan sinyal D2 dengan value HIGH
			usb.write("up"); #MCU akan mengirim value ke USB dengan menggunakan fungsi usb.write()
		elif digitalRead(3) == HIGH: #digitalRead mendapatkan sinyal dari D3. Jika button Down ditekan maka button akan mengirimkan sinyal D3 dengan value HIGH
			usb.write("down"); #MCU akan mengirim value ke USB dengan menggunakan fungsi usb.write()
		else:
			usb.write("stop"); #MCU akan mengirim value ke USB dengan menggunakan fungsi usb.write()
		
		delay(500)

if __name__ == "__main__":
	main()