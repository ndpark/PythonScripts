import sys

theBoard={'top-L':' ','top-M':' ','top-R':' ',
		  'mid-L':' ','mid-M':' ','mid-R':' ',
		  'low-L':' ','low-M':' ','low-R':' '}
		  
def printBoard(board):
	print(board['top-L']+'|' + board['top-M'] + '|' + board['top-R'] )
	print('-+-+-')
	print(board['mid-L']+'|' + board['mid-M'] + '|' + board['mid-R'] )
	print('-+-+-')
	print(board['low-L']+'|' + board['low-M'] + '|' + board['low-R'] )

def whoWon(theBoard):
	while True:
		if ((theBoard['top-L'] == 'X'and theBoard['top-M'] == 'X'and theBoard['top-R'] == 'X') or
			(theBoard['mid-L'] == 'X'and theBoard['mid-M'] == 'X'and theBoard['mid-R'] == 'X') or
			(theBoard['low-L'] == 'X'and theBoard['low-M'] == 'X'and theBoard['low-R'] == 'X') or
			(theBoard['top-L'] == 'X'and theBoard['mid-M'] == 'X'and theBoard['low-R'] == 'X') or
			(theBoard['bot-L'] == 'X'and theBoard['mid-M'] == 'X'and theBoard['top-R'] == 'X')):
			print('\n\nPlayer X, you won!')
			sys.exit()
		elif((theBoard['top-L'] == 'O'and theBoard['top-M'] == 'O'and theBoard['top-R'] == 'O') or
			(theBoard['mid-L'] == 'O'and theBoard['mid-M'] == 'O'and theBoard['mid-R'] == 'O') or
			(theBoard['low-L'] == 'O'and theBoard['low-M'] == 'O'and theBoard['low-R'] == 'O') or
			(theBoard['top-L'] == 'O'and theBoard['mid-M'] == 'O'and theBoard['low-R'] == 'O') or
			(theBoard['bot-L'] == 'O'and theBoard['mid-M'] == 'O'and theBoard['top-R'] == 'O')):
			print('\n\nPlayer O, you won!')
			sys.exit()

turn = 'X'

for i in range(9):
	whoWon(theBoard)
	printBoard(theBoard) #Prints the board at each turn
	print('Turn for ' + turn+'. Move on which space?' )
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn='X'	
printBoard(theBoard)