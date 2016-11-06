#!flask/bin/python
from flask import Flask, jsonify
app = Flask(__name__)

from sensors.laser import Laser as Laser
from sensors.lcd import Lcd as Lcd
from sensors.ultrasonic_ranging import UltrasonicRanging as Ultrasound

laserPointer = Laser()
ultrasoundSensor = Ultrasound()
LcdScreen = Lcd()

@app.route('/sensor/laser/<on>')
def laser(on):
    if on == '1':
        laserPointer.turnOn()
    elif on == '0':
        laserPointer.turnOff()
    return jsonify(True)

@app.route('/sensor/ultrasound')
def ultrasound():
    return jsonify(ultrasoundSensor.getDistanceInCm())

@app.route('/sensor/lcd/<row1>/<row2>')
def lcd(row1, row2):
    LcdScreen.setUpperText(row1)
    LcdScreen.setLowerText(row2)
    return jsonify(True)

@app.route('/sensor/lcd/<x>/<y>/<text>')
def lcdAtLocation():
    LcdScreen.setTextAtLocation(int(x), int(y), text)
    return jsonify(True)

@app.route('/sensor/lcd/clear')
def lcdClear():
    LcdScreen.clearDisplay()
    return jsonify(True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
