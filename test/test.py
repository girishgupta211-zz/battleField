import unittest
from BattleField import BattleField
class TestBattleArea(unittest.TestCase):

	def test_battlearea_returns_correct_result(self):
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

		test_battleArea = BattleArea(9, 'E')
		test_battleArea.createBattleArea()
		self.assertNotEqual([
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		], test_battleArea.battleArea)

if __name__ == '__main__':
	unittest.main() 