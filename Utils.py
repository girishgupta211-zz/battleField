class Utils():
	@staticmethod
	def convertToCartesian(targetLocations):
		return [ (ord(location[0]) - 64 , location[1]) for location in targetLocations]

	@staticmethod
	def toAlphaNumeric(location):	
		return (chr(64+location[0]) , location[1])