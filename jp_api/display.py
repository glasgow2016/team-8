from sensors.lcd import Lcd as Lcd
from otpcode.otp import OTP as otp
from sensors.laser import Laser as Laser
from sensors.ultrasonic_ranging import UltrasonicRanging as Ultrasound
import time
import RPi.GPIO as GPIO

GPIO.setWarnings(False)
LcdScreen = Lcd()
codeGenerator = otp('patch of grass')
laserPointer = Laser()
ultrasoundSensor = Ultrasound()

def run():
    timeout = -1
    while True:
        if timeout > 0 and time.time() - timeout < 30:
            LcdScreen.setUpperText('Hi! Your code is')
            LcdScreen.setLowerText('     ' + codeGenerator.getCode() + '     ')
            laserPointer.turnOn()
            time.sleep(2)
        else:
            if ultrasoundSensor.getDistanceInCm() < 50:
                timeout = time.time()
            else:
                timeout = -1
                LcdScreen.clearDisplay()
                laserPointer.turnOff()

def close():
    LcdScreen.clearDisplay()
    laserPointer.turnOff()

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        close()
