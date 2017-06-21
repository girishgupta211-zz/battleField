import unittest
import sys
from Player import Player
from Utils import Utils

class TestBattleAreaBase(unittest.TestCase):

	def test_battlearea_returns_correct_result(self):
		width,heigth,battleShipsArr1,battleShipsArr2,targetsForPlayer1,targetsForPlayer2 = Utils.parse('input/input2.txt')
		winStatus = Player.startGame(width,heigth,battleShipsArr1,battleShipsArr2,targetsForPlayer1,targetsForPlayer2)		
		self.assertEqual(winStatus, False)

if __name__ == '__main__':
	unittest.main() 