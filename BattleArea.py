from BattleAreaBase import BattleAreaBase
class BattleArea(BattleAreaBase):
	""" This class is used to create battle field with battle ships
		It is having a attribute totalPower which shows total power of batter field
		whcih is sum of power of all active cell where 
		battle ships are kept(1 for P and 2 for Q type) """
	# totalPower = 0
	def __init__(self, m,n,battleShipArry):
		BattleAreaBase.__init__(self,m,n)	
		self.battleShipArray = battleShipArry
		self.createBattleAreaBase()		
		self.populateBattleArea()		
	
	def _checkBattleShipBoundry(self,location, dimension, type ):		
		if ( ord(location[0]) - 64 + dimension[0]-1 > self.maxX or  location[1] +dimension[1]-1 > self.maxY):
			raise Exception("battleShip should be within battle field dimension of " + str(self.maxX) + " by " + str(self.maxY))	
	

	def populateBattleArea(self):		
		power = dict(P = 1 , Q = 2 )
		for battleShip in self.battleShipArray:
			self._checkBattleShipBoundry(battleShip["location"],battleShip["dimension"],battleShip["type"])
			x = battleShip["location"][1]
			# convert width from aphabet to number
			y = ord(battleShip["location"][0]) - 64			
			xRange = [ x + i  for i in range(battleShip["dimension"][0]) ]
			yRange = [ y + i  for i in range(battleShip["dimension"][1]) ]						
			for i in yRange:
				for j in xRange:
					# Set 1 or 2 depending upon ship type in cell
					self.battleArea[i-1][j-1] = power[battleShip["type"]]
					# Add power to totalPower as per type
					self.totalPower +=  power[battleShip["type"]]