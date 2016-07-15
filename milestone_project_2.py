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
from random import randint

class Player(object):
	
	card_map = {'one':1, 'two':2, 'three':3, 
				'four':4, 'five':5, 'six':6,
				'seven':7, 'eight':8, 'nine':9,
				'ten':10, 'jack':10, 'queen':10,
				'king':10, 'ace':11}

	def __init__(self,bankroll=100):
		self.bankroll = bankroll
		self.wins = 0
		self.losses =0
		self.hand = []
		self.handvalue = 0
		self.ace_count = 0

	def adjust_bankroll(self,amount):
		self.bankroll += amount

	def add_card(self,card):
		self.hand.append(card)
		self.handvalue += Player.card_map[card]
		if self.handvalue > 21 and self.hand.count('ace') > self.ace_count:
			self.handvalue -= 10
			self.ace_count += 1

	def clear_hand(self):
		self.hand = []
		self.handvalue = 0
		self.ace_count = 0
		
	def print_hand(self):
		print "You have the following cards: "
		for card in self.hand:
			print card
		print "For a total of: {}".format(self.handvalue)


class Deck(object):
	card_list = ['two', 'two', 'two', 'two',
			'three', 'three', 'three', 'three',
			'four', 'four', 'four', 'four',
			'five', 'five', 'five', 'five',
			'six', 'six', 'six', 'six',
			'seven', 'seven', 'seven', 'seven',
			'eight', 'eight', 'eight', 'eight',
			'nine', 'nine', 'nine', 'nine',
			'ten', 'ten', 'ten', 'ten',
			'jack', 'jack', 'jack', 'jack',
			'queen', 'queen', 'queen', 'queen',
			'king', 'king', 'king', 'king',
			'ace', 'ace', 'ace', 'ace']

	def __init__(self):
		self.cards = Deck.card_list

	def draw_card(self):
		"""
		Method generates a random number that is used to return a card
		from the deck. The card is then popped from the list and the card
		is returned to the user.
		"""
		card_number = randint(0,len(self.cards)-1)
		card = self.cards[card_number]
		self.cards.pop(card_number)
		return card

	def shuffle_deck(self):
		self.cards = Deck.card_list

	def __str__(self):
		return str(self.cards)
	
	def __len__(self):
		return len(self.cards)

brad = Player(10)
#print brad.wins
#print brad.losses
#print brad.bankroll

deck_0 = Deck()
print len(deck_0)
#print deck_0
#print deck_0.cards
brad.add_card(deck_0.draw_card())
brad.add_card(deck_0.draw_card())
brad.add_card(deck_0.draw_card())
brad.print_hand()

