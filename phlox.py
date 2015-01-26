#!/usr/bin/python
import nixie
import pi
import RPi.GPIO as GPIO
import time
from bitstring import BitStream, BitArray

# Take care if you wire using BOARD or BCM notation

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def tubePrint( tube, intNum ):
	"Prints passed integer to a tube connected to a gpio set"
	# The tube is turned off if the number is greater than 9
	if intNum > 9:
		for i in range(0, 4):
			GPIO.setup(pi.Tubes[tube][i],GPIO.IN)
	else:
		bnum = BitArray(bin = nixie.nums[intNum])
		for i in range(0, 4):
			GPIO.setup(pi.Tubes[tube][i],GPIO.OUT)
			GPIO.output(pi.Tubes[tube][i],bnum[i])
	return

def disBlank():
	"Prints 10 on all tubes, effectively turrning them off"
	for tube in range(1, 5):
		tubePrint(tube,10)
	return

def disPrint( intNum ):
	"Prints a number 0-9999 on the four tubes"
	cTube = 4
# prints the digits in reverse turning off remaining tubes 
# incidentally this won't print 0:00 - 0:59 correctly but that's ok 
# for now since I have it off at 23:59 :)
	for digit in [int(i) for i in str(intNum)[::-1]]:
		tubePrint( cTube, digit )
		cTube -= 1
	while (cTube >= 1):
		tubePrint( cTube, 10 )
		cTube -= 1
	return


disBlank()
# A little start-up animation
for i in range(1, 5):
	tubePrint(5-i,i)
	time.sleep(0.3)
	disBlank()

for i in [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999 ]:
	disPrint(i)
	time.sleep(0.3)

disBlank()
time.sleep(0.3)

# The shut-off time is hardcoded here
while True:
	cTime=int(time.strftime('%H%M'))
	if cTime >= 730 and cTime <= 2359:
		disPrint(cTime)
	else:
		disBlank()
	time.sleep(1)

