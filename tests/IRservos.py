#!/usr/bin/python3

from adafruit_servokit import ServoKit
from time import sleep
import socket

debug = False

# init the ir socket connection
SOCKPATH = "/var/run/lirc/lircd"

sock = None

def init_irw():
    global sock
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    print ('starting up on %s' % SOCKPATH)
    sock.connect(SOCKPATH)

# init the servo connection
kit = ServoKit(channels=16)

x = 15
y = 14

xLoc = 90
yLoc = 120

kit.servo[x].angle = xLoc
kit.servo[y].angle = yLoc

def next_key():
    '''Get the next key pressed. Return keyname, updown.
    '''
    while True:
        data = sock.recv(128)
        # print("Data: " + data)
        data = data.strip()
        if data:
            break

    words = data.split()
    return words[2], words[1]

if __name__ == '__main__':
    init_irw()

    while True:
        #get the keypress
        keyname, updown = next_key()
        #print debug info
        if(debug): print(keyname)
        #look for direction keys
        if(str(keyname) == str(b'KEY_DOWN')):
            if(yLoc < 179): yLoc = yLoc + 2
        if(str(keyname) == str(b'KEY_UP')):
            if(yLoc > 1): yLoc = yLoc - 2
        if(str(keyname) == str(b'KEY_RIGHT')):
            if(xLoc < 180): xLoc = xLoc + 2
        if(str(keyname) == str(b'KEY_LEFT')):
            if(xLoc > 1): xLoc = xLoc - 2
        
        kit.servo[x].angle = xLoc
        kit.servo[y].angle = yLoc
