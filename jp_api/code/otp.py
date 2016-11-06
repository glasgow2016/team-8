import pyotp
import base64

class OTP:

    def __init__(self, secret):
        self.totp = pyotp.TOTP(base64.b32encode(secret))

    def getCode(self):
        return self.totp.now()

    def verifyCode(self, code):
        return self.totp.verify(code)