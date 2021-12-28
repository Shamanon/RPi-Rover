#!/usr/bin/python3

# Read and display voltage from V.Sensor connected to 
# MCP3008 A/D conversion unit

from gpiozero import MCP3008, LED
from time import sleep

ledG = LED(5)
ledR = LED(6)
pin = 7
pot = MCP3008(pin,max_voltage=5.04)

#for loop to read all pins
#for x in range(0,8):
#	print(MCP3008(x,max_voltage=5.04).voltage)

while 1:
	volt = round((pot.voltage+pot.voltage+pot.voltage)/3, 4)
	V = round(volt/0.2, 1)
	if float(V)>11: 
		ledG.on()
		ledR.off()
	else:
		ledR.on()
		ledG.off()
	#return battery voltage
	print("Battery: ",V, end='\r')
	sleep(1)
