import LCD1602
import time

def __init__(self):
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.write(0, 0, 'Testing')
	LCD1602.write(1, 1, '1234567890')
	time.sleep(2)
	LCD1602.clear()

def setUpperText(self, text):
	LCD1602.write(0, 0, text)

def setLowerText(self, text):
	LCD1602.write(1, 1, text)

def clearDisplay(self):
	LCD1602.clear()

def setTextAtLocation(self, x, y, text):
	LCD1602.write(x, y, text)
