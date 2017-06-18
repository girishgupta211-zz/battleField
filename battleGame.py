import string
from pprint import pprint 
from BattleArea import BattleArea
from BattleShip import BattleShip
from BattleField import BattleField
from ast import literal_eval

def convertToCartesian(targetLocations):
	return [ (ord(location[0]) - 64 , location[1]) for location in targetLocations]

def toAlphaNumeric(location):	
	return (chr(64+location[0]) , location[1])

def hitMissile(battleField,target):	
	# check if target shell is an active shell( having power (1 or 2))	
	if(battleField.battleArea[target[0]-1][target[1]-1] > 0):
		battleField.battleArea[target[0]-1][target[1]-1] -= 1
		battleField.totalPower -= 1
		return True
	else:
		return False

class Player():
	"""docstring for Player"""
	def __init__(self, battleField,targetMissiles):
		self.battleField = battleField
		self.targetMissiles = targetMissiles

def createBattleShips(ships,m,n):	
	battleShips = []
	for ship in ships:			
		location = literal_eval(ship['location'])
		dimension = literal_eval(ship['dimension'])
		battleShips.append(BattleShip(location,dimension,ship['type'],m,n))
	return battleShips


def run():
		# Pass json file as input
	import json
	j = open('player2Won.json', 'r')
	data = json.load(j)	
	# pprint (data)
	m = data['m']
	n = data['n']
	
	battleShipsArea1 = createBattleShips(data['tank1'],m,n)
	battleShipsArea2 = createBattleShips(data['tank2'],m,n)
	
	battleField1 = BattleField(m,n,battleShipsArea1)
	battleField2 = BattleField(m,n,battleShipsArea2)

	targetsPlayer1 = convertToCartesian(list(literal_eval(data['missileTargetsForPlayerA'])))
	targetsPlayer2 = convertToCartesian(list(literal_eval(data['missileTargetsForPlayerB'])))

	player1 = Player(battleField1,targetsPlayer1)
	player2 = Player(battleField2,targetsPlayer2)
	
	play(player1, player2)
	# pprint (player1.battleField.battleArea)
	# pprint (player2.battleField.battleArea)

def play(player1,player2):	
# def play(battleField1,battleField2,targetsPlayer1,targetsPlayer2):	
	currPlayer = 1 
	status = False
	while(True):
		if(player1.battleField.totalPower == 0):
			print ("Player-2 won the battle")
			break
		if(player2.battleField.totalPower == 0):
			print ("Player-1 won the battle")
			break

		if(len(player1.targetMissiles) == 0 and len(player2.targetMissiles) == 0):
			print ("Player-1 and Player-2 have no more missiles left. players declare peace.")
			break

		if(len(player1.targetMissiles) == 0):
			print ("Player-1 no more missiles left")
			currPlayer = 2			

		if(len(player2.targetMissiles) == 0):
			print ("Player-2 no more missiles left")
			currPlayer = 1			

		# print targetsPlayer1
		if(currPlayer == 1):
			target = player1.targetMissiles.pop(0)			
			status = hitMissile(player2.battleField, target)
			if(status):
				print ("Player-1 fires a missile with target " +  str(toAlphaNumeric(target)) + " which hit")
				currPlayer = 1				
			else:
				print ("Player-1 fires a missile with target " +  str(toAlphaNumeric(target)) + " which missed")
				currPlayer = 2
			
		else:	
			target = player2.targetMissiles.pop(0)			
			status = hitMissile(player1.battleField, target)
			if(status):
				print ("Player-2 fires a missile with target " +  str(toAlphaNumeric(target)) + " which hit")
				currPlayer = 2			
			else:
				print ("Player-2 fires a missile with target " +  str(toAlphaNumeric(target)) + " which missed")
				currPlayer = 1
	
if __name__ == '__main__':
	run()
