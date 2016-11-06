import pyotp

class OTP:

    def __init__(self, secret):
        self.totp = pyotp.TOTP(secret)

    def getCode(self):
        return self.totp.now()

    def verifyCode(self, code):
        return self.totp.verify(code)