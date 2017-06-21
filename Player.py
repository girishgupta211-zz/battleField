from Utils import Utils
from BattleArea import BattleArea
class Player(object):
	"""
	This represents a player. Each player own a battle Field 
	and target missiles that would be hit on opponent 
	"""
	def __init__(self, width,heigth,battleShipsArray,targetMissiles):
		self.battleArea = BattleArea(width,heigth,battleShipsArray)
		self.targetMissiles = targetMissiles

	@staticmethod	
	def _hitMissile(battleArea,target,currPlayer):

		"""
		hits the target cell on opponent player by current player
		if target cell is active (having 1/2 power), then return curent player
		if target cell is not active(having 1 power), then return other player
		"""
	# check if target shell is an active shell( having power (1 or 2))			
		if(battleArea.battleArea[target[0]-1][target[1]-1] > 0):
			battleArea.battleArea[target[0]-1][target[1]-1] -= 1
			battleArea.totalPower -= 1			
			print ("Player-" + str(currPlayer) +  "  fires a missile with target " +  str(Utils.toAlphaNumeric(target)) + " which got hit")
			return currPlayer

		else:
			print ("Player-" + str(currPlayer) +  "  fires a missile with target " +  str(Utils.toAlphaNumeric(target)) + " which got miss")			
			return 2 if currPlayer == 1 else 1

	def _playerWin(player1,player2):
		"""
		if any player is having total power == 0 , then opponent wins the match
		"""
		if(player1.battleArea.totalPower == 0):
			print ("Player-2 won the battle")
			return True
			
		if(player2.battleArea.totalPower == 0):
			print ("Player-1 won the battle")
			return True

	def _checkNoMissiles(player1,player2, currPlayer):
			"""
			if both players having no missiles left then they declare peace
			if any one of player has no missiles left, then chances goes to other player
			"""
			if(len(player1.targetMissiles) == 0 and len(player2.targetMissiles) == 0):
				print ("Player-1 and Player-2 have no more missiles left to launch. players declare peace.")
				return 0			

			if(len(player1.targetMissiles) == 0):
				print ("Player-1 no more missiles left to launch")
				return 2

			if(len(player2.targetMissiles) == 0):
				print ("Player-2 no more missiles left to launch")
				return 1

			return currPlayer

	def playBattle(player1,player2):	
		"""
			Start game with player1. play in infinite loop, till either missiles are finished from both side
			or total power is 0 of any player
		"""	
		currPlayer = 1	

		while(True):

			if(Player._playerWin(player1,player2) == True):
				return True

			status = Player._checkNoMissiles(player1,player2,currPlayer)
			
			# if no missiles left
			if(status == 0):
				return False

			if(status == 1 or status == 2) :
				currPlayer = status
							

			if(currPlayer == 1):
				target = player1.targetMissiles.pop(0)			
				currPlayer = Player._hitMissile(player2.battleArea, target, currPlayer)
				
			else:	
				target = player2.targetMissiles.pop(0)
				currPlayer = Player._hitMissile(player1.battleArea, target,currPlayer)

	@staticmethod	
	def startGame(width,heigth,battleShipsArr1,battleShipsArr2,targetsForPlayer1,targetsForPlayer2):
		player1 = Player(width,heigth,battleShipsArr1,targetsForPlayer1)
		player2 = Player(width,heigth,battleShipsArr2,targetsForPlayer2)
		status = Player.playBattle(player1, player2)
		return status
