import string
from pprint import pprint 
from BattleArea import BattleArea
from BattleShip import BattleShip
from BattleField import BattleField
from ast import literal_eval
from Utils import Utils


class Player():
	"""docstring for Player"""
	def __init__(self, battleField,targetMissiles):
		self.battleField = battleField
		self.targetMissiles = targetMissiles

	@staticmethod
	def hitMissile(battleField,target,currPlayer):	
	# check if target shell is an active shell( having power (1 or 2))	
		if(battleField.battleArea[target[0]-1][target[1]-1] > 0):
			battleField.battleArea[target[0]-1][target[1]-1] -= 1
			battleField.totalPower -= 1			
			print ("Player-" + str(currPlayer) +  "  fires a missile with target " +  str(Utils.toAlphaNumeric(target)) + " which hit")
			return currPlayer

		else:
			print ("Player-" + str(currPlayer) +  "  a missile with target " +  str(Utils.toAlphaNumeric(target)) + " which missed")
			return 2 if currPlayer == 1 else 1


def checkWinCriteria(player1,player2):
		if(player1.battleField.totalPower == 0):
			print ("Player-2 won the battle")
			return True
			
		if(player2.battleField.totalPower == 0):
			print ("Player-1 won the battle")
			return True
			
def checkNoMissiles(player1,player2):
		if(len(player1.targetMissiles) == 0 and len(player2.targetMissiles) == 0):
			print ("Player-1 and Player-2 have no more missiles left. players declare peace.")
			return 0			

		if(len(player1.targetMissiles) == 0):
			print ("Player-1 no more missiles left")
			return 2

		if(len(player2.targetMissiles) == 0):
			print ("Player-2 no more missiles left")
			return 1	



def createBattleShips(ships,m,n):	
	battleShips = []
	for ship in ships:			
		location = literal_eval(ship['location'])
		dimension = literal_eval(ship['dimension'])
		battleShips.append(BattleShip(location,dimension,ship['type'],m,n))
	return battleShips



def playBattle(player1,player2):	
	currPlayer = 1	

	while(True):

		if(checkWinCriteria(player1,player2)):
			break

		currPlayer = checkNoMissiles(player1,player2)

		if(currPlayer == 0):
			break

		if(currPlayer == 1):
			target = player1.targetMissiles.pop(0)			
			currPlayer = player1.hitMissile(player2.battleField, target, currPlayer)
			
		else:	
			target = player2.targetMissiles.pop(0)			
			currPlayer = player2.hitMissile(player1.battleField, target,currPlayer)

def run():
	# Pass json file as input
	import json
	j = open('player2Won.json', 'r')
	# j = open('input2.json', 'r')
	data = json.load(j)		
	m = data['m']
	n = data['n']
	
	battleShipsArea1 = createBattleShips(data['tank1'],m,n)
	battleShipsArea2 = createBattleShips(data['tank2'],m,n)
	
	battleField1 = BattleField(m,n,battleShipsArea1)
	battleField2 = BattleField(m,n,battleShipsArea2)

	targetsPlayer1 = Utils.convertToCartesian(list(literal_eval(data['missileTargetsForPlayerA'])))
	targetsPlayer2 = Utils.convertToCartesian(list(literal_eval(data['missileTargetsForPlayerB'])))

	player1 = Player(battleField1,targetsPlayer1)
	player2 = Player(battleField2,targetsPlayer2)
	
	playBattle(player1, player2)

	
if __name__ == '__main__':
	run()
