#####################################################
#
#	DO NOT WATCH THE LASER DERECTELY IN THE EYE!
#
#####################################################
import RPi.GPIO as GPIO
import time

class Laser:

	def __init__(self):
		self.LedPin = 11
		GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
		GPIO.setup(self.LedPin, GPIO.OUT)   # Set LedPin's mode is output
		GPIO.output(self.LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

	def turnOn(self):
		GPIO.output(self.LedPin, GPIO.LOW)

	def turnOff(self):
		GPIO.output(self.LedPin, GPIO.HIGH)

	def destroy(self):
		GPIO.output(self.LedPin, GPIO.HIGH)     # led off
		GPIO.cleanup()                     # Release resource
