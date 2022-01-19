#!/usr/bin/python3
# coding: utf-8

## control pan and tilt of head with controlller

# Load the gamepad and time libraries
import Gamepad
import time
from adafruit_servokit import ServoKit
from gpiozero import TonalBuzzer, LED, Tone

# GPIO Zero settings
b = TonalBuzzer(20)
led = LED(26)

# init the servo connection
kit = ServoKit(channels=16)

x = 15
y = 14

xLoc = 90
yLoc = 120

kit.servo[x].angle = xLoc
kit.servo[y].angle = yLoc

# Gamepad settings
gamepadType = Gamepad.PS3
buttonHappy = 'CROSS'
buttonBeep = 'CIRCLE'
buttonExit = 'PS'
joystickSpeed = 'RIGHT-Y'
joystickSteering = 'RIGHT-X'
pollInterval = 0.2

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Set some initial state
global running
global beepOn
global speed
global steering
running = True
beepOn = False
speed = 0.0
steering = 0.0

# Create some callback functions
def happyButtonPressed():
    led.on()

def happyButtonReleased():
    led.off()

def beepButtonChanged(isPressed):
    global beepOn
    beepOn = isPressed

def exitButtonPressed():
    global running
    print('EXIT')
    running = False

def speedAxisMoved(position):
    global speed
    speed = -position   # Inverted

def steeringAxisMoved(position):
    global steering
    steering = position # Non-inverted


# Start the background updating
gamepad.startBackgroundUpdates()

# Register the callback functions
gamepad.addButtonPressedHandler(buttonHappy, happyButtonPressed)
gamepad.addButtonReleasedHandler(buttonHappy, happyButtonReleased)
gamepad.addButtonChangedHandler(buttonBeep, beepButtonChanged)
gamepad.addButtonPressedHandler(buttonExit, exitButtonPressed)
gamepad.addAxisMovedHandler(joystickSpeed, speedAxisMoved)
gamepad.addAxisMovedHandler(joystickSteering, steeringAxisMoved)

# Keep running while joystick updates are handled by the callbacks
try:
    while running and gamepad.isConnected():
        # Show the current speed and steering
        print('%+.1f %% speed, %+.1f %% steering' % (speed * 100, steering * 100))
        
        #move the head
        yLoc = round(120 + (30 * speed))
        xLoc = round(90 + (90 * steering))
        kit.servo[x].angle = xLoc
        kit.servo[y].angle = yLoc
        

        # Display the beep if held
        if beepOn:
            for i in range(60,70):
                b.play(Tone(midi=float(i))) # frequency
                time.sleep(.1)
            b.stop()

        # Sleep for our polling interval
        time.sleep(pollInterval)
finally:
    # Ensure the background thread is always terminated when we are done
    gamepad.disconnect()
