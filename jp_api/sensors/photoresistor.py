import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

class PhotoResistor:

	def __init__(self):
		self.DO = 11
		GPIO.setmode(GPIO.BOARD)
		ADC.setup(0x48)
		GPIO.setup(self.DO, GPIO.IN)

	def getLightValue(self):
		return ADC.read(1)

	def destroy(self):
		GPIO.cleanup()
