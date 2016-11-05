import Adafruit_DHT as DHT
import RPi.GPIO as GPIO

class Humiture:
	def __init__(self):
		self.Sensor = 11
		self.humiture = 17

	def getTemperatureInCeluis(self):
		humidity, temperature = DHT.read_retry(self.Sensor, self.humiture)
		if humidity is not None and temperature is not None:
			return '{0:0.1f}'.format(temperature)
		else:
			return None

	def getHumidityInPercent(self):
		humidity, temperature = DHT.read_retry(self.Sensor, self.humiture)
		if humidity is not None and temperature is not None:
			return '{0:0.1f}'.format(humidity)
		else:
			return None

	def destroy(self):
		GPIO.cleanup()
