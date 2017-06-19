import string
from pprint import pprint 
from BattleArea import BattleArea
from BattleField import BattleField
from Player import Player
from ast import literal_eval
from Utils import Utils

def run():
	# Pass json file as input
	import json
	j = open('input/player2Won.json', 'r')
	# j = open('input2.json', 'r')
	data = json.load(j)		
	m = data['m']
	n = data['n']
	
	battleShipsArea1 = Utils.createBattleShips(data['tank1'],m,n)
	battleShipsArea2 = Utils.createBattleShips(data['tank2'],m,n)
	
	battleField1 = BattleField(m,n,battleShipsArea1)
	battleField2 = BattleField(m,n,battleShipsArea2)

	targetsPlayer1 = Utils.convertToCartesian(list(literal_eval(data['missileTargetsForPlayerA'])))
	targetsPlayer2 = Utils.convertToCartesian(list(literal_eval(data['missileTargetsForPlayerB'])))

	player1 = Player(battleField1,targetsPlayer1)
	player2 = Player(battleField2,targetsPlayer2)
	
	Player.playBattle(player1, player2)

	
if __name__ == '__main__':
	run()
