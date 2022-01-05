#  ___   ___  ___  _   _  ___   ___   ____ ___  ____  
# / _ \ /___)/ _ \| | | |/ _ \ / _ \ / ___) _ \|    \ 
#| |_| |___ | |_| | |_| | |_| | |_| ( (__| |_| | | | |
# \___/(___/ \___/ \__  |\___/ \___(_)____)___/|_|_|_|
#                  (____/ 
# Osoyoo Raspberry Pi start Kit Lesson 19: IR control
# tutorial url: https://osoyoo.com/2017/07/07/ir-remote/
import RPi.GPIO as GPIO
from time import time
LED1=18 #LED 1 in physical Pin 18 
LED2=22 #LED 2 in physical Pin 22
LED3=7  #LED 3 in physical Pin 7 
status1=0
status2=0
status3=0
IR_PIN=12 #IR pin in physical Pin 12 

KEY_1=0xff30cf
KEY_2=0xff18e7
KEY_3=0xff7a85

def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.setup(LED3, GPIO.OUT)


def binary_aquire(pin, duration):
    # aquires data as quickly as possible
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results


def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_aquire(pinNo, bouncetime/1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i
    # decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
    # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None


def destroy():
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        print("Starting IR Listener")
        while True:
            print("Waiting for signal")
            GPIO.wait_for_edge(IR_PIN, GPIO.FALLING)
            code = on_ir_receive(IR_PIN)
            if (code==KEY_1):
                if (status1==0):
                   status1=1
                   GPIO.output(LED1, GPIO.HIGH)
                else:
                   status1=0
                   GPIO.output(LED1, GPIO.LOW)
            elif (code==KEY_2):
                if (status2==0):
                   status2=1
                   GPIO.output(LED2, GPIO.HIGH)
                else:
                   status2=0
                   GPIO.output(LED2, GPIO.LOW)
            elif (code==KEY_3):
                if (status3==0):
                   status3=1
                   GPIO.output(LED3, GPIO.HIGH)
                else:
                   status3=0
                   GPIO.output(LED3, GPIO.LOW)
            else:
                print("Invalid code")
    except KeyboardInterrupt:
        # User pressed CTRL-C
        # Reset GPIO settings
        print("Ctrl-C pressed!")
    except RuntimeError:
        # this gets thrown when control C gets pressed
        # because wait_for_edge doesn't properly pass this on
        pass
    print("Quitting")
    destroy()
