#####################################################
#
#	DO NOT WATCH THE LASER DERECTELY IN THE EYE!
#
#####################################################
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

def __init__(self):
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def turnOn(self):
	GPIO.output(LedPin, GPIO.LOW)

def turnOff(self):
	GPIO.output(LedPin, GPIO.HIGH)

def destroy(self):
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource
