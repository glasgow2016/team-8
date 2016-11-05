#!flask/bin/python
from flask import Flask, jsonify
app = Flask(__name__)

from sensors.laser import Laser as laser
from sensors.lcd import Lcd as Lcd
from sensors.ultrasonic_ranging import UltrasonicRanging as ultrasound

@app.route('/sensor/laser/<on>')
def laser(on):
    laserPointer = laser()
    if on == '1':
        laserPointer.turnOn()
    elif on == '0':
        laserPointer.turnOff()
    return jsonify(True)

@app.route('/sensor/ultrasound')
def ultrasound():
    ultrasoundSensor = ultrasound()
    return jsonify(ultrasoundSensor.getDistanceInCm())

@app.route('/sensor/lcd/<row1>/<row2>')
def lcd(row1, row2):
    LcdScreen = Lcd()
    LcdScreen.setUpperText(row1)
    LcdScreen.setLowerText(row2)
    return jsonify(True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
