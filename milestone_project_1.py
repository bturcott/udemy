#Milestone Project 1
#By Brad
#Tic Tac Toe Game
"""
Tic Tac Toe
X X X
X X X
X X X 
"""

def game_loop():
	print 'Welcome to Tic Tac Toe!!'
	selection = 'yes'
	while selection == 'yes':
		tic_tac_toe()
		selection = raw_input("enter 'yes' if you would like to play again: ")
		print selection
	print 'Goodbye!'

def tic_tac_toe():
	gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]
	print_board(gameboard)
	for i in range(0,9):
		if i % 2 == 0:
			print 'Player 1 select a space'
			row = input("Enter the row number (0-2): ")
			while row < 0 or row > 2:
				row = input("Enter a row number between 0 and 2: ")
			column = input("Enter the column (0-2): ")
			while column < 0 or column > 2:
				column = input("Enter a column number between 0 and 2: ")
			while gameboard[row][column] != '-':
				print 'Please select a vacant space'
				row = input("Enter the row number (0-2): ")
				column = input("Enter the column (0-2): ")
			gameboard[row][column] = 'X'
			if check_board(gameboard,row,column) == True:
				print_board(gameboard)
				print 'Player 1 has won!'
				break
		else:
			print 'Player 2 select a space'
			row = input("Enter the row number (0-2): ")
			while row < 0 or row > 2:
				row = input("Enter a row number between 0 and 2: ")
			column = input("Enter the column (0-2): ")
			while column < 0 or column > 2:
				column = input("Enter a column number between 0 and 2: ")
			while gameboard[row][column] != '-':
				print 'Please select a vacant space'
				row = input("Enter the row number (0-2): ")
				column = input("Enter the column (0-2): ")
			gameboard[row][column] = 'O'
			if check_board(gameboard,row,column) == True:
				print_board(gameboard)
				print 'Player 2 has won!'
				break
		print_board(gameboard)
	print 'The game resulted in a tie!'

def print_board(board):
	"""
	Function that prints the Tic Tac Toe board
	"""
	print "  0       1      2"
	print " -------------------"
	print "0| {}      {}      {} |".format(board[0][0],board[0][1],board[0][2])
	print "1| {}      {}      {} |".format(board[1][0],board[1][1],board[1][2])
	print "2| {}      {}      {} |".format(board[2][0],board[2][1],board[2][2])
	print " -------------------"


#Three checks need to occur - the row, the column and diagonal if row and column == 1
def check_board(board,row,column):
	if board[row][0] == board[row][1] == board[row][2]:
		return True
	elif board[0][column] == board[1][column] == board[2][column]:
		return True
	elif board[0][0] == board[1][1] == board[2][2] == board[row][column]:
		return True
	elif board[0][2] == board[1][1] == board[2][0] == board[row][column]:
		return True
	return False


game_loop()