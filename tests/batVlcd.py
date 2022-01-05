#!/usr/bin/python3

# Import LCD library
from RPLCD import i2c
from gpiozero import MCP3008, LED
import time
from time import sleep

# v sensor opts
ledG = LED(5)
ledR = LED(6)
pin = 7
pot = MCP3008(pin,max_voltage=5.04)

# constants to initialise the LCD
lcdmode = 'i2c'
cols = 16
rows = 2
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1 
address = 0x27 
port = 1 # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)

lcd.close(clear=True)

while 1:
	d = time.strftime('%l:%M%p %m.%d.%y')
	volt = round((pot.voltage+pot.voltage+pot.voltage)/3, 4)
	V = round(volt/0.2, 1)
	if float(V)>9.9: 
		ledG.on()
		ledR.off()
	else:
		ledR.on()
		ledG.off()
	#return battery voltage
	lcd.write_string(d)
	lcd.crlf()
	lcd.write_string('Batery: ')
	lcd.write_string(str(V))
	lcd.write_string('V  ')
	lcd.crlf()
	print("Battery: ",V, end='\r')
	lcd.close(clear=False)
	sleep(10)

# Write a string on first line and move to next line
#lcd.write_string('BYE!')
#sleep(10)
# Switch off backlight
#lcd.backlight_enabled = False 
# Clear the LCD screen
