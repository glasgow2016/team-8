import Adafruit_DHT as DHT
import RPi.GPIO as GPIO

Sensor = 11
humiture = 17

def __init__(self):
	pass

def getTemperatureInCeluis(self):
	humidity, temperature = DHT.read_retry(Sensor, humiture)
	if humidity is not None and temperature is not None:
		return '{0:0.1f}'.format(temperature)
	else:
		return None

def getHumidityInPercent(self):
	humidity, temperature = DHT.read_retry(Sensor, humiture)
	if humidity is not None and temperature is not None:
		return '{1:0.1f}'.format(humidity)
	else:
		return None

def destroy(self):
	GPIO.cleanup()
