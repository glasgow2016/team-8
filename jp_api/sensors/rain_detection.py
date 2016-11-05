#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math

class RainDetection:

	DO = 17

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		ADC.setup(0x48)
		GPIO.setup(DO, GPIO.IN)

	def isRaining(self):
		return not GPIO.input(DO)

	def getRawRainValue(self):
		return ADC.read(0)
