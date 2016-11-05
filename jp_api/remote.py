#!flask/bin/python
from flask import Flask
app = Flask(__name__)

import sensors.humiture as humiture
import sensors.rain_detection as rain_detection
import sensors.photoresistor as photoresistor
import sensors.rgb_led as rgb_led

@app.route('/')
def index():
    return "Hey! Human"

@app.route('/sensor/humidity')
def humidity():
    humiditySensor = humiture()
    return humiditySensor.getHumidityInPercent()

@app.route('/sensor/temperature')
def temperature():
    humiditySensor = humiture()
    return humiditySensor.getTemperatureInCeluis()

@app.route('/sensor/rain')
def rain():
    rainSensor = rain_detection()
    return rainSensor.isRaining()

@app.route('/sensor/light')
def light():
    lightSensor = photoresistor()
    return lightSensor.getLightValue()

@app.route('/sensor/led/<r>/<g>/<b>')
def led(r, g, b):
    rgbLed = rgb_led()
    return rgbLed.setColor(r, g, b)

if __name__ == '__main__':
    app.run(debug=True)
