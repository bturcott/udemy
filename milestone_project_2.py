"""
Project: Blackjack Game
By: Brad Turcott
Requirements:
	- One player vs automated dealer
	- Player can stand or hit
	- Player must be able to choose bet amount
	- Keep track of players total money
	- Alert of wins,losses, or busts
	- Use classes!
"""

class Player(object):
	wins = 0
	losses = 0
	
	def __init__(self,bankroll=100):
		self.bankroll = bankroll

	def adjust_bankroll(self,amount):
		self.bankroll += amount

class Deck(object):
	card_list = ['one','one','one','one',
			'two', 'two', 'two', 'two',
			'three', 'three', 'three', 'three',
			'four', 'four', 'four', 'four',
			'five', 'five', 'five', 'five',
			'six', 'six', 'six', 'six', 'six',
			'seven', 'seven', 'seven', 'seven',
			'eight', 'eight', 'eight', 'eight',
			'nine', 'nine', 'nine', 'nine',
			'ten', 'ten', 'ten', 'ten',
			'jack', 'jack', 'jack', 'jack',
			'queen', 'queen', 'queen', 'queen',
			'king', 'king', 'king', 'king',
			'ace', 'ace', 'ace', 'ace']
			
	card_map = {'one':1, 'two':2, 'three':3, 
				'four':4, 'five':5, 'six':6,
				'seven':7, 'eight':8, 'nine':9,
				'ten':10, 'jack':10, 'queen':10,
				'king':10, 'ace':[11,1]}
	
	def __init__(self):
		self.cards = Deck.card_list

	def draw_card(self):
		

	def shuffle_deck(self):
		self.cards = Deck.card_list

brad = Player(10)
print brad.wins
print brad.losses
print brad.bankroll

