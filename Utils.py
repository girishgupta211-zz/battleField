from ast import literal_eval
from BattleShip import BattleShip

class Utils():
	@staticmethod
	def convertToCartesian(targetLocations):
		return [ (ord(location[0]) - 64 , location[1]) for location in targetLocations]

	@staticmethod
	def toAlphaNumeric(location):	
		return (chr(64+location[0]) , location[1])

	@staticmethod
	def createBattleShips(ships,m,n):
		"""
		Used to create indivisual battle ship from initial location, dimention and type
		"""
		battleShips = []
		for ship in ships:			
			location = literal_eval(ship['location'])
			dimension = literal_eval(ship['dimension'])
			battleShips.append(BattleShip(location,dimension,ship['type'],m,n))
		return battleShips
