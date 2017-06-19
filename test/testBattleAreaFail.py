import unittest
from BattleArea import BattleArea
class TestBattleArea(unittest.TestCase):

	def test_battlearea_returns_correct_result(self):
		test_battleArea = BattleArea(4, 'E')
		test_battleArea.createBattleArea()
		self.assertNotEqual([
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		], test_battleArea.battleArea)

if __name__ == '__main__':
	unittest.main() 
