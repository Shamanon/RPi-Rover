#!/usr/bin/python3

from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

a = 15
b = 14
c = 13

kit.servo[a].angle = 180
sleep(2)
kit.servo[a].angle = 0
sleep(2)
kit.servo[a].angle = 90

kit.servo[b].angle = 160
sleep(2)
kit.servo[b].angle = 0
sleep(2)
kit.servo[b].angle = 130

kit.servo[c].angle = 180
sleep(2)
kit.servo[c].angle = 0
sleep(2)
kit.servo[c].angle = 90

