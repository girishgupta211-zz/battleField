import string
from pprint import pprint 

def validateRange(func):
	def inner_func(self,X, Y):
		if X > 9:
			raise Exception("M needs to be less than 9")		
		if( Y not in list(string.ascii_uppercase)):
			raise Exception( "N should be between 'A' and 'Z' (Capital letter Only)" )		
		
		return func(self,X,Y)
	return inner_func


class BattleArea():
	@validateRange
	def __init__(self,maxX,maxY):		
		self.maxX = maxX
		self.maxY = ord(maxY) - 64

	def createBattleArea(self):
		self.battleArea = [ [0 for i in xrange(self.maxX)] for i in xrange(self.maxY) ]