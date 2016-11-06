from sensors.lcd import Lcd as Lcd
from otpcode.otp import OTP as otp
from sensors.laser import Laser as Laser
from sensors.ultrasonic_ranging import UltrasonicRanging as Ultrasound
import time

LcdScreen = Lcd()
codeGenerator = otp('patch of grass')

def run():

    timeout = -1
    while True:
        if timeout > 0 and time.time() - timeout < 30:
            LcdScreen.setUpperText('Hi! Your code is')
            LcdScreen.setLowerText('     ' + codeGenerator.getCode() + '     ')
            Laser().turnOn()
            time.sleep(2)
        else:
            if Ultrasound().getDistanceInCm() < 140:
                timeout = time.time()
            else:
                timeout = -1
                LcdScreen.clearDisplay()
                Laser().turnOff()

def close():
    LcdScreen.clearDisplay()

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        close()
