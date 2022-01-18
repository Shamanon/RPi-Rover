#!/usr/bin/python3

from gpiozero import LED
from time import sleep

led1 = LED(13)

led1.on()
sleep(10)
led1.off()
