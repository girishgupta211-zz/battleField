import unittest
import sys
sys.path.append('../')
from BattleAreaBase import BattleAreaBase
class TestBattleAreaBase(unittest.TestCase):

	def test_battlearea_returns_correct_result(self):
		test_battleArea = BattleAreaBase(4, 'D')
		test_battleArea.createBattleAreaBase()
		self.assertEqual([
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		], test_battleArea.battleArea)

if __name__ == '__main__':
	unittest.main() 