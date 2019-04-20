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

def isWinStateMiniSquare(state, mini_square, player):
	'''
	A mini-square is in win_state if either any cols,
	any rows or any diag is successfully filled by a 
	single player
	params:
	state - obj of stateObject class
	mini_square - int for mini_square in board
	player - macro for player
	'''
	mini_board = getMiniBoard(state, mini_square)
	win_states = [
	[mini_board[0][0], mini_board[0][1], mini_board[0][2]],
	[mini_board[1][0], mini_board[1][1], mini_board[1][2]],
	[mini_board[2][0], mini_board[2][1], mini_board[2][2]],
	[mini_board[0][0], mini_board[1][0], mini_board[2][0]],
	[mini_board[0][1], mini_board[1][1], mini_board[2][1]],
	[mini_board[0][2], mini_board[1][2], mini_board[2][2]],
	[mini_board[0][0], mini_board[1][1], mini_board[2][2]],
	[mini_board[0][2], mini_board[1][1], mini_board[2][0]]
	]
	print(win_states)
	if [player, player, player]	in win_states:
		return True
	else:
		return False

def isWinState(state, player):
	'''
	function to check if Complete board is in win state.
	A win state is reached when any row, any col or any diag 
	of mini_squares is won by a single player
	params:
	state - obj of stateObject class
	player - macro for deciding player
	'''
	win_states = [
		[(state, 1, player), (state, 4, player), (state, 7, player)],
		[(state, 2, player), (state, 5, player), (state, 8, player)],
		[(state, 3, player), (state, 6, player), (state, 9, player)],
		[(state, 1, player), (state, 2, player), (state, 3, player)],
		[(state, 4, player), (state, 5, player), (state, 6, player)],
		[(state, 7, player), (state, 8, player), (state, 9, player)],
		[(state, 7, player), (state, 5, player), (state, 3, player)],
		[(state, 1, player), (state, 5, player), (state, 9, player)],
	]
	for win_state in win_states:
		is_valid_win_state = []
		for params in win_state:
			print(params)
			_ = input('sdfdsf')
			is_valid_win_state.append(isWinStateMiniSquare(*params))
		print(is_valid_win_state)
		_ = input('sdfdsf')
		if all(is_valid_win_state):
			return True
	return False

def declareWinner(player):
	'function to declare the player passed as winner'
	if player == HUMAN:
		print('Congrats! You Won.')
	else:
		print('You lost.')

def play(state, player, first_run=False):
	'''
	Function that runs the game
	params:
	state - object of stateObject class, containing details about current
			state of game
	player - Macros for player
	first_run - kwarg
	'''
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
		return False
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
			valid_mini_square = [move]
			updateMoveOnBoard(state, player, mini_square, move)
			displayBoard(state)
		else:
			# aiMove(state)
			_ = input('Press to pass AI turn ')
			return False
		## Checking for win or draw state
		if isWinState(state, player): 
			displayBoard(state)
			declareWinner(player)
			return True
		elif isDrawState(state):  ## Not defined yet
			pass
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
	play(state, player, first_run=True)
	while not done:
		player *= -1
		done = play(state, player)

if __name__ == '__main__':
	main()