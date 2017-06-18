from BattleArea import BattleArea
class BattleField(BattleArea):
	totalPower = 0
	def __init__(self, m,n,battleShipArry):
		BattleArea.__init__(self,m,n)
		self.createBattleArea()		
		self.populateBattleField(battleShipArry)
	
	def populateBattleField(self,battleShipArry):		
		for tank in battleShipArry:
			x = tank.location[1]
			y =ord(tank.location[0]) - 64			
			xRange = [ x + i  for i in range(tank.dimention[0]) ]
			yRange = [ y + i  for i in range(tank.dimention[1]) ]			
			power = { 'P':1 , 'Q':2 }			
			for i in xRange:
				for j in yRange:
					self.battleArea[i-1][j-1] = power[tank.type]
					self.totalPower += power[tank.type]
		# pprint.pprint (self.battleArea)

