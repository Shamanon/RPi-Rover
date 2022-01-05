#!/usr/bin/python3

from gpiozero import LED
from time import sleep

led1 = LED(5)
led2 = LED(6)
led3 = LED(26)
led4 = LED(19)

#while True:
#    led1.on()
#    led2.off()
#    sleep(1)
#    led1.off()
#    led2.on()
#    sleep(1)

led3.on()
led4.on()
sleep(10)
