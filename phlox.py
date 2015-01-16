#!/usr/bin/python
import nixie
import pi
import RPi.GPIO as GPIO
import time
from bitstring import BitStream, BitArray

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def tubePrint( tube, intNum ):
	"Prints passed integer to a tube connected to gpio set"
	bnum = BitArray(bin = nixie.nums[intNum])
	for i in range(0, 4):
		GPIO.output(pi.Tubes[tube][i],bnum[i])
	return

def disPrint( intNum ):
	"Prints a number 0-9999 on the four tubes"
	tube = 1
	for digit in [int(i) for i in str(intNum)]:
#		print "Digit: ", digit, " - ", tube
		tubePrint( tube, digit )
		tube += 1
	return

for GPIOP in pi.GPIOS:
	GPIO.setup(GPIOP,GPIO.OUT)

for GPIOP in pi.GPIOS:
	GPIO.output(GPIOP,GPIO.LOW)

while True:
	disPrint(int(time.strftime('%H%M')));
	time.sleep(1)

