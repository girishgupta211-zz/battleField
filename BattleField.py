from BattleArea import BattleArea
class BattleField(BattleArea):
	""" This class is used to create battle field with battle ships
		It is having a attribute totalPower which shows total power of batter field
		whcih is sum of power of all active cell where 
		battle ships are kept(1 for P and 2 for Q type) """
	# totalPower = 0
	def __init__(self, m,n,battleShipArry):
		BattleArea.__init__(self,m,n)	
		self.createBattleArea()		
		self.populateBattleField(battleShipArry)		
	
	def populateBattleField(self,battleShipArry):		
		power = dict(P = 1 , Q = 2 )
		for tank in battleShipArry:
			x = tank.location[1]
			y = ord(tank.location[0]) - 64			
			xRange = [ x + i  for i in range(tank.dimention[0]) ]
			yRange = [ y + i  for i in range(tank.dimention[1]) ]						
			for i in xRange:
				for j in yRange:
					# Set 1 or 2 depending upon ship type in cell
					self.battleArea[i-1][j-1] = power[tank.type]
					# Add power to totalPower as per type
					self.totalPower += power[tank.type]	