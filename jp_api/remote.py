#!flask/bin/python
from flask import Flask, jsonify
app = Flask(__name__)

from sensors.humiture import Humiture as humiture
from sensors.rain_detection import RainDetection as rain_detection
from sensors.photoresistor import PhotoResistor as photoresistor
from sensors.rgb_led import RgbLed as rgb_led

humiditySensor = humiture()
rainSensor = rain_detection()
lightSensor = photoresistor()
rgbLed = rgb_led()

@app.route('/sensor/humidity')
def humidity():
    return jsonify(humiditySensor.getHumidityInPercent())

@app.route('/sensor/temperature')
def temperature():
    return jsonify(humiditySensor.getTemperatureInCeluis())

@app.route('/sensor/rain')
def rain():
    return jsonify(rainSensor.isRaining())

@app.route('/sensor/light')
def light():
    return jsonify(lightSensor.getLightValue())

@app.route('/sensor/led/<r>/<g>/<b>')
def led(r, g, b):
    rgbLed.setColor(r, g, b)
    return jsonify(True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
