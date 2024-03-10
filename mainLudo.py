import random


# Below is a class to create the players, and it includes the playername, and also the pieces and their counts in a dictionary
class Player:
	def __init__(self, name, color):
		self.name = name
		self.pieces = 4
		self.dict = {1: 57, 2: 57, 3: 57, 4: 57}
		self.color = color


# this part of the code allows players to input their usernames and the player objects are created from the class
player1 = Player(input('Player1, enter your username: '), 'red')
player2 = Player(input('Player2, enter your username: '), 'blue')


# function to give the players context about the game and let them know the rules of the game
def Rules():
	print('\nWelcome to Ludo Version2. Each player has 4 pieces, each with an initial count of 57.')
	print('You need to roll a 6 when you want to get each piece out of home.'
	      'You also get to roll the die each time you roll a 6.\nGet all your piece counts to 0 to win the game! Goodluck.\n')


# function to roll the die, specific to each player. Player 1 enters r1 and player2 enters r2 to roll die
def rollDice(playing):
	if playing == player1:
		user = input('Press r1 to roll the die: ').lower()
		while user != 'r1':  # Allows the user to enter the correct input instead of forfeiting their chance or getting an error
			print('invalid input')
			user = input('Press r1 to roll the die: ')
	else:
		user = input('Press r2 to roll the die: ').lower()  # makes sure that the input is not case sensitive
		while user != 'r2':
			print('invalid input!')
			user = input('press r2 to roll the die: ')
	value = random.randint(1, 6)
	print('you got a', value)
	return value


# function to switch the players turns
def switchPlayers(playing):
	if playing == player1:
		print('\n', player2.name, 'you are now playing')
		return player2
	else:
		print('\n', player1.name, 'you are now playing')
		return player1


# function to check for the winner
def checkWin(player):
	values = []
	for counts in player.dict.values():
		values.append(counts)
	if values == [0, 0, 0, 0]:
		print(player.name, 'wins the game!')
		return True  # return false


# function to choose which piece to move and also displays the pieces and the counts/steps
def choosePiece(player):
	print('This is the status of your pieces: ', player.dict)
	while True:
		selectPiece = input('Choose which piece to move: 1,2,3 or 4 ')
		if selectPiece in ['1', '2', '3', '4']:  # to ensure that they input 1,2,3 or 4 and anything else will result
			# in the prompt'Invalid input'
			break
		else:
			print('Invalid Input. Try again ')  # allow them to enter the correct input
	return int(selectPiece)


# function to move the selected piece
def movePiece(player, piece, die_value):
	print('Piece', piece, 'will move', die_value, 'steps')
	player.dict[piece] -= die_value


# function that will return all active pieces
def active(player):
	active = []
	for pieces in player.dict:
		if 0 < player.dict[pieces] < 57:
			active.append(pieces)
	return active


def ludo2():
	playing = player1
	Rules()
	print(playing.name, 'will start')
	# function to play a piece that is either active or inactive
	while True:
		die_value = rollDice(playing)  # player will roll the die first
		
		while die_value == 6:  # when they roll a 6, they get into this while loop and only leave when they roll a non-6
			pieceChosen = choosePiece(playing)  # asking them to choose a piece to move
			
			while playing.dict[
				pieceChosen] == 0:  # this line of code makes sure that players can not move a piece that has won
				print(pieceChosen, 'already at home. Choose another piece')
				pieceChosen = choosePiece(playing)
			
			if pieceChosen in active(playing):  # to check if the piece chosen if now active or out of home
				if playing.dict[pieceChosen] - die_value < 0:
					print("Count exceeded. You can't move piece", pieceChosen)
					break
				else:
					movePiece(playing, pieceChosen, die_value)
					if checkWin(playing):
						break
			else:
				playing.dict[pieceChosen] -= 1  # reduce the count of that piece
				print('piece', pieceChosen, 'out of home')
			die_value = rollDice(playing)
		
		if die_value != 6 and active(playing) != []:  # if player rolls a non-6, and have some of their pieces active
			pieceChosen = choosePiece(playing)
			
			# while loop to make sure that they choose a piece that is out of home and lets player know
			while pieceChosen not in active(playing):
				print("You can't move piece", pieceChosen, '.It is inactive')
				pieceChosen = choosePiece(playing)
			
			if playing.dict[pieceChosen] - die_value < 0:
				print("Count exceeded. You can't move piece", {pieceChosen})
			else:
				movePiece(playing, pieceChosen, die_value)
		
		if checkWin(playing) == True:  # checking is the player has won
			break
		
		playing = switchPlayers(playing)  # switching the players

ludo2()
