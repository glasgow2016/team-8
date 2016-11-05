import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

DO = 17

def __init__(self):
	GPIO.setmode(GPIO.BCM)
	ADC.setup(0x48)
	GPIO.setup(DO, GPIO.IN)

def getLightValue(self):
	return ADC.read(1)
