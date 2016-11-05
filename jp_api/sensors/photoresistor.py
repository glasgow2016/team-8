import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

class PhotoResistor:

	def __init__(self):
		self.DO = 17
		GPIO.setmode(GPIO.BCM)
		ADC.setup(0x48)
		GPIO.setup(self.DO, GPIO.IN)

	def getLightValue(self):
		return ADC.read(1)
