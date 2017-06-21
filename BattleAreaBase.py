import string

def validateRange(func):
	""" Decortaor used to validate X and Y range  """
	def checkBounds(self,X, Y):
		if X > 9 or X < 1:
			raise Exception("M needs to be less than 9 and greater than 0")		
		if( Y not in list(string.ascii_uppercase)):
			raise Exception( "N should be between 'A' and 'Z' (Capital letter Only)" )		
		
		return func(self,X,Y)
	return checkBounds


class BattleAreaBase(object):
	""" This class is used to create an empty battle Area(battleArea) with MXN Grid with zeors   """
	@validateRange	
	def __init__(self,maxX,maxY):		
		self.maxX = maxX
		self.maxY = ord(maxY) - 64 # convert Alphabet to number so that it can be easily processed as array
		self.battleArea = []
		self.totalPower = 0

	def createBattleAreaBase(self):
		self.battleArea = [ [0 for i in xrange(self.maxX)] for i in xrange(self.maxY) ]
