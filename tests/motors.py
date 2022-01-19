#!/usr/bin/python3
# test motor controller

from gpiozero import Motor
from time import sleep

motorR = Motor(17, 27)
motorL = Motor(24, 23)

motorR.forward(0.5)
sleep(1)
motorR.reverse()
sleep(1)
motorR.stop()

motorL.forward(0.5)
sleep(1)
motorL.reverse()
sleep(1)
motorL.stop()
