from sensors.lcd import Lcd as Lcd
from code.otp import OTP as otp

LcdScreen = Lcd()
codeGenerator = otp('patch of grass')

def setup():
    LcdScreen.setUpperText('Hi! Your code is')

def run():
    while True:
        LcdScreen.setLowerText('     ' + codeGenerator.getCode() + '     ')

def close():
    LcdScreen.clearDisplay()

if __name__ == "__main__":
    try:
        setup()
        run()
    except KeyboardInterrupt:
        close()
