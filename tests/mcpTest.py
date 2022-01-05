#!/usr/bin/python3

# Read and display voltage from all devices on
# MCP3008 A/D conversion unit

from gpiozero import MCP3008
from time import sleep

#for loop to read all pins
for x in range(0,8):
	print(MCP3008(x,max_voltage=5.04).voltage)

