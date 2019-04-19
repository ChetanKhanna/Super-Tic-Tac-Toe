'''
Roadmap: 1) Make super-tic-tac-toe with random move selector
		 2) Add minmax algorithm
		 3) Improve minmax algorithm with alpha beta pruning
'''

# Importing useul modules
import random
import os
import copy
from math import inf
from pprint import pprint

# Defining important vairables
board = [
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
	[[None, None, None],
	 [None, None, None],
	 [None, None, None]
	],
]
HUMAN = 1
COMPUTER = -1
cell_to_pos = {
	1:[0,0], 2:[0,1], 3:[0,2],
	4:[1,0], 5:[1,1], 6:[1,2],
	7:[2,0], 8:[2,1], 9:[2,2]
}
valid_mini_square = []

class stateObject:
	
	def __init__(self, state):
		self.state = state
		self.val = None
		self.parent = None
		self.role = None

def getMiniBoard(state, mini_square):
	mini_board = {
		1:state.state[0], 2:state.state[1], 3:state.state[2],
		4:state.state[3], 5:state.state[4], 6:state.state[5],
		7:state.state[6], 8:state.state[7], 9:state.state[8]
	}
	return mini_board[mini_square]

def displayMiniBoard(mini_board):
	for row in mini_board:
		pprint(row)

def displayBoard(state):
	for i in range(3):
		for j in range(3):
			for k in range(i*3, (i+1)*3):
				print(state.state[k][j], end = ' | ')
			print()
		print('---------------------'*3)

def updateMoveOnBoard(state, player, mini_square, move):
	r, c = cell_to_pos[move]
	mini_board = getMiniBoard(state, mini_square)
	mini_board[r][c] = player

def isValidMove(state, mini_square, cell):
	r, c = cell_to_pos[cell]
	mini_board = getMiniBoard(state, mini_square)
	if not mini_board[r][c]:
		return True
	else:
		return False

def declareWinner(player):
	if player == HUMAN:
		print('Congrats! You Won.')
	else:
		print('You lost.')

def play(state, player, first_run=False):
	global valid_mini_square
	if first_run:
		os.system('clear')
		print('Your turn')
		displayBoard(state)
		mini_square = -1
		while mini_square < 1 or mini_square > 9:
			mini_square = int(input('select mini_square: '))
		displayMiniBoard(state.state[mini_square])
		move = -1
		while move < 1 or move > 9:
			move = int(input('Select cell 1:9: '))
		valid_mini_square = [move]
		updateMoveOnBoard(state, player, mini_square, move)
		displayBoard(state)

	else:
		if player == HUMAN:
			os.system('clear')
			print('Your turn')
			# Display entire board
			displayBoard(state)
			# Selecting mini square
			mini_square = -1
			print('Following mini_square are available:\n', valid_mini_square)
			if len(valid_mini_square) > 1:
				print('Select one to play:')
				while mini_square not in valid_mini_square:
					mini_square = int(input('select mini_square: '))
			else:
				mini_square = valid_mini_square.pop()
			displayMiniBoard(state.state[mini_square])
			# selecting move in mini square
			move = -1
			while move < 1 or move > 9:
				move = int(input('Select cell 1:9: '))
				if not isValidMove(state, mini_square, move):
					print('Move invalid! Try again.')
					move = -1

			updateMoveOnBoard(state, player, mini_square, move)
			displayBoard(state)
		else:
			aiMove(state)
	## Checking for win or draw state
	if isWinState(state, player):  ## Not defined yet
		displayBoard(state)
		declareWinner(player)
		return True
	elif isDrawState(state):  ## Not defined yet
		print('Match Tied!')
		displayBoard(state)
		return True
	else:
		return False			

def main():
	'''
	Controller function for the game.
	'''
	global board, mini_board
	done = False
	player = HUMAN
	state = stateObject(board)
	play(state, player, first_run=False)
	while not done:
		done = play(state, player)
		player *= -1

if __name__ == '__main__':
	main()