import unittest
from BattleField import BattleField
from ast import literal_eval
from Utils import Utils
from Player import Player

class TestBattleArea(unittest.TestCase):

	def test_battlearea_returns_correct_result(self):
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
		
		winStatus = Player.playBattle(player1, player2)	
	
		self.assertEqual(winStatus, True)

if __name__ == '__main__':
	unittest.main() 