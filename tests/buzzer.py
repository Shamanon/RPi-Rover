#!/usr/bin/python3

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

b = TonalBuzzer(20)

for i in range(60,70):
	b.play(Tone(midi=float(i))) # frequency
	sleep(.1)

#for i in range(220,440):
#	b.play(Tone(frequency=int(i))) # frequency
#	sleep(.01)

