#!/usr/bin/python3
# test motor controller

from gpiozero import Motor
import Gamepad
from time import sleep

debug = False

# motor settings
motorR = Motor(17, 27)
motorL = Motor(24, 23)

# Gamepad settings
gamepadType = Gamepad.PS3
buttonExit = 'CROSS'
joystickSpeed = 'LEFT-Y'
joystickSteering = 'LEFT-X'
pollInterval = 0.3

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Set some initial state
global running
global speed
global steering
running = True
speed = 0.0
steering = 0.0

# functions to put stick values in variables
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
gamepad.addButtonPressedHandler(buttonExit, exitButtonPressed)
gamepad.addAxisMovedHandler(joystickSpeed, speedAxisMoved)
gamepad.addAxisMovedHandler(joystickSteering, steeringAxisMoved)

# Keep running while joystick updates are handled by the callbacks
try:
	while running and gamepad.isConnected():
		# Show the current speed and steering
		if(debug): print('%+.1f %% speed, %+.1f %% steering' % (speed, steering))
		
		if(steering > 0 and speed > 0 or steering < 0 and speed < 0):
			r = speed - steering
			l = speed
		elif(steering < 0 and speed > 0 or speed < 0 and steering > 0):
			r = speed
			l = speed + steering
		elif(speed == 0):
			r = steering * -1
			l = steering
		else: 
			r = speed
			l = speed	

		if(l > 0):
			motorL.forward(l)
		elif(l < 0):
			motorL.backward(l * -1)
		else:
			motorL.stop()

		if(r > 0):
			motorR.forward(r)
		elif(r < 0):
			motorR.backward(r * -1)
		else:
			motorR.stop()



		# Sleep for our polling interval
		sleep(pollInterval)
finally:
    # Ensure the background thread is always terminated when we are done
    gamepad.disconnect()
