#!/usr/bin/python3

from gpiozero import LED

led1 = LED(26)

while 1:
	led1.on()
