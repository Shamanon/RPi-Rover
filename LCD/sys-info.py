#!/usr/bin/env python3
# Display battery, cpu, mem, wifi, time, date on LCD
# 2022 by Joshua Besneatte https://piratesinteepees.org
# Freeware

# Import LCD library
from RPLCD import i2c
# LED Control
from gpiozero import MCP3008, LED
# Libs
import time
import signal
import sys
import psutil

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

#This will capture exit when using Ctrl-C
def handle_ctrl_c(signal, frame):
	print('\b\bGoodbye.')
	sys.exit(130)
 
signal.signal(signal.SIGINT, handle_ctrl_c)

def sysinfo():
    # Get cpu statistics
    cpu = str("{:02d}".format(round(psutil.cpu_percent()))) + '%  '
    lcd.write_string('C')
    lcd.write_string(cpu)
    # Calculate memory information
    memory = psutil.virtual_memory()
    mem_info = str(round(memory.percent)) + '%  '
    lcd.write_string('M')
    lcd.write_string(mem_info)
    # Calculate disk information
    disk = psutil.disk_usage('/')
    disk_info = str(round(disk.percent)) + '%'
    lcd.write_string('D')
    lcd.write_string(disk_info)
    
def voltage():
    volt = round((pot.voltage+pot.voltage+pot.voltage)/3, 4)
    V = round(volt/0.2)
    if float(V)>9.9: 
        ledG.on()
        ledR.off()
    else:
        ledR.on()
        ledG.off()
    #write to LCD
    lcd.write_string(str(V) + 'V')
    
#main loop
while 1:
    #Write time/date to LCD
    d = time.strftime('%H:%M %m/%d  ')
    lcd.write_string(d)
    #Write voltage to LCD
    voltage()
    lcd.crlf()
    #Write system info to LCD
    sysinfo()
    lcd.crlf()	
    lcd.close(clear=False)
    time.sleep(10)

