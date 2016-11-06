import LCD1602

class Lcd:

	def __init__(self):
		LCD1602.init(0x27, 1)	# init(slave address, background light)
		LCD1602.clear()

	def setUpperText(self, text):
		LCD1602.write(0, 0, text)

	def setLowerText(self, text):
		LCD1602.write(0, 1, text)

	def clearDisplay(self):
		LCD1602.clear()

	def setTextAtLocation(self, x, y, text):
		LCD1602.write(x, y, text)
