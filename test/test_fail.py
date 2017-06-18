import unittest
from BattleArea import BattleArea
class TestBattleField(unittest.TestCase):

	def test_battlefield_returns_correct_result(self):
		test_battlefield = BattleArea(4, 'E')
		test_battlefield.createBattleArea()
		self.assertNotEqual([
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		], test_battlefield.battleArea)

if __name__ == '__main__':
	unittest.main() 
