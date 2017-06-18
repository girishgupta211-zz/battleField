def validateBattleShip(func):
	def inner_func(self,location, dimention, type,maxX,maxY ):		
		x =ord(location[0]) - 64
		y = location[1]		

		if ( x+dimention[0]-1 > maxX or  y+dimention[1]-1 > ord(maxY) - 64):
			raise Exception("battleShip should be within battle field dimention of " + str(maxX) + " by " + str(maxY))
	
		return func(self,location,dimention,type,maxX,maxY)
	return inner_func


class BattleShip():
	@validateBattleShip
	def __init__(self, location, dimention,type,maxX,maxY):				
		self.location = location
		self.dimention = dimention
		self.type = type		
