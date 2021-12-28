#!/usr/bin/python3

from gpiozero import LED
from time import sleep

#led1 = LED(5)
#led2 = LED(6)
#led3 = LED(4)

for x in range(0,9):
    led = LED(x)
    print("Testing LED:",x)
    led.on()
    sleep(1)
    led.off()
