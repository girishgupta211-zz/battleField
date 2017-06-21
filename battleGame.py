import sys
from Player import Player
from Utils import Utils




def main(fileName):
	try:
		width,heigth,battleShipsArr1,battleShipsArr2,targetsForPlayer1,targetsForPlayer2 = Utils.parse(fileName)
		Player.startGame(width,heigth,battleShipsArr1,battleShipsArr2,targetsForPlayer1,targetsForPlayer2)

	except Exception as e:
		raise e

if __name__ == '__main__':
	filename = 'input/input.txt'
	main(filename)
	# main(sys.argv[1])



