from Utils import Utils
class Player(object):
	"""
	This represents a player. Each player own a battle Field 
	and target missiles that would be hit on opponent 
	"""
	def __init__(self, battleField,targetMissiles):
		self.battleField = battleField
		self.targetMissiles = targetMissiles

	@staticmethod	
	def hitMissile(battleField,target,currPlayer):	
		"""
		hits the target cell on opponent player by current player
		if target cell is active (having 1/2 power), then return curent player
		if target cell is not active(having 1 power), then return other player
		"""
	# check if target shell is an active shell( having power (1 or 2))	
		if(battleField.battleArea[target[0]-1][target[1]-1] > 0):
			battleField.battleArea[target[0]-1][target[1]-1] -= 1
			battleField.totalPower -= 1			
			print ("Player-" + str(currPlayer) +  "  fires a missile with target " +  str(Utils.toAlphaNumeric(target)) + " which hit")
			return currPlayer

		else:
			print ("Player-" + str(currPlayer) +  "  a missile with target " +  str(Utils.toAlphaNumeric(target)) + " which missed")
			return 2 if currPlayer == 1 else 1

	def playerWin(player1,player2):
		"""
		if any player is having total power == 0 , then opponent wins the match
		"""
		if(player1.battleField.totalPower == 0):
			print ("Player-2 won the battle")
			return True
			
		if(player2.battleField.totalPower == 0):
			print ("Player-1 won the battle")
			return True

	def checkNoMissiles(player1,player2):
			"""
			if both players having no missiles left then they declare peace
			if any one of player has no missiles left, then chances goes to other player
			"""
			if(len(player1.targetMissiles) == 0 and len(player2.targetMissiles) == 0):
				print ("Player-1 and Player-2 have no more missiles left. players declare peace.")
				return 0			

			if(len(player1.targetMissiles) == 0):
				print ("Player-1 no more missiles left")
				return 2

			if(len(player2.targetMissiles) == 0):
				print ("Player-2 no more missiles left")
				return 1

	def playBattle(player1,player2):	
		"""
			Start game with player1. play in infinite loop, till either missiles are finished from both side
			or total power is 0 of any player
		"""	
		currPlayer = 1	

		while(True):

			if(Player.playerWin(player1,player2) == True):
				return True

			currPlayer = Player.checkNoMissiles(player1,player2)

			# if no missiles left
			if(currPlayer == 0):
				return False

			if(currPlayer == 1):
				target = player1.targetMissiles.pop(0)			
				currPlayer = Player.hitMissile(player2.battleField, target, currPlayer)
				
			else:	
				target = player2.targetMissiles.pop(0)			
				currPlayer = Player.hitMissile(player1.battleField, target,currPlayer)