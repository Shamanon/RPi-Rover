#!/usr/bin/python3

from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

kit.servo[0].angle = 180
sleep(2)
kit.servo[0].angle = 0
sleep(2)
kit.servo[0].angle = 90

kit.servo[1].angle = 180
sleep(2)
kit.servo[1].angle = 0
sleep(2)
kit.servo[1].angle = 110

