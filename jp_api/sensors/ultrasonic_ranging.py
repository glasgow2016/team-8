#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


class UltrasonicRanging:

	TRIG = 15
	ECHO = 16

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(TRIG, GPIO.OUT)
		GPIO.setup(ECHO, GPIO.IN)

	def getDistanceInCm(self):
		GPIO.output(TRIG, 0)
		time.sleep(0.000002)

		GPIO.output(TRIG, 1)
		time.sleep(0.00001)
		GPIO.output(TRIG, 0)

		while GPIO.input(ECHO) == 0:
			a = 0
		time1 = time.time()

		while GPIO.input(ECHO) == 1:
			a = 1
		time2 = time.time()

		during = time2 - time1
		return during * 340 / 2 * 100

	def destroy(self):
		GPIO.cleanup()
