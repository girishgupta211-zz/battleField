class Utils():
	"""
	Simple utility function used across all the classes
	"""

	@staticmethod
	def toAlphaNumeric(location):	
		return (chr(64+location[0]) , location[1])

	@staticmethod
	def getCordinates(position):
		cordinates = list(position)
		return (cordinates[0], int(cordinates[1]))	

	@staticmethod
	def getCordinatesCartition(position):
		cordinates = list(position)
		return (ord(cordinates[0])-64, int(cordinates[1]))

	@staticmethod
	def parse(file):
		try:
			lines = [ line.strip().split(' ') for line in open(file, 'r').xreadlines() ]
			cordinates = lines[0]
			width  = int(cordinates[0])
			heigth = cordinates[1]

			battleShipsCount = int(lines[1][0])

			battleShipsArr1 = list()
			battleShipsArr2 = list()
			for i in range(0,int(battleShipsCount)):
				type, w,h, positions1,positions2 = lines[2+i]
				battleShipsArr1.append({"dimension":(int(w),int(h)) , "location":Utils.getCordinates(positions1) , "type": type})
				battleShipsArr2.append({"dimension":(int(h),int(h)) , "location":Utils.getCordinates(positions2) , "type": type})
			
			targetsForPlayer1 = [ Utils.getCordinatesCartition(x) for x in  lines[battleShipsCount+2]]
			targetsForPlayer2 = [ Utils.getCordinatesCartition(x) for x in  lines[battleShipsCount+3]]	
			return width,heigth,battleShipsArr1,battleShipsArr2,targetsForPlayer1,targetsForPlayer2

		except Exception as e:
			print ("Please pass a valid input file specified in problem statement \n")
			raise e