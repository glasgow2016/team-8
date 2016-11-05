#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math

class RainDetection:

	def __init__(self):
		self.DO = 11
		GPIO.setmode(GPIO.BOARD)
		ADC.setup(0x48)
		GPIO.setup(self.DO, GPIO.IN)

	def isRaining(self):
		return not GPIO.input(self.DO)

	def getRawRainValue(self):
		return ADC.read(0)

	def destroy(self):
		GPIO.cleanup()
