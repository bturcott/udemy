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
from time import sleep

class Player(object):
	
	card_map = {'one':1, 'two':2, 'three':3, 
				'four':4, 'five':5, 'six':6,
				'seven':7, 'eight':8, 'nine':9,
				'ten':10, 'jack':10, 'queen':10,
				'king':10, 'ace':11}

	def __init__(self,bankroll=100,name="Dealer"):
		self.bankroll = bankroll
		self.name = name
		self.wins = 0
		self.losses =0
		self.hand = []
		self.handvalue = 0
		self.ace_count = 0
		self.bet = 0

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
		self.bet = 0
		
	def print_hand(self):
		string = "You have the following cards: "
		for card in self.hand:
			string += card + ", "
		print string[0:len(string)-2]
		print "For a total of: {}".format(self.handvalue)

	def __str__(self):
		return str(self.name)


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

def game_setup(user,dealer,deck):
	"""
	Clears the players hands and shuffles the deck
	"""
	user.clear_hand()
	dealer.clear_hand()
	deck.shuffle_deck()
	print "Cards have been collected and the deck has been shuffled!"
	print "You have {} dollars in chips.".format(user.bankroll)
	user.bet = int(raw_input("Enter the amount you wish to bet: "))
	user.bankroll -= user.bet
	inital_deal(user,dealer,deck)

def inital_deal(user,dealer,deck):
	sleep(1.5)
	card = deck.draw_card()
	print user, "has drawn a {}".format(card)
	user.add_card(card)
	sleep(1.5)
	card = deck.draw_card()
	print dealer, "has drawn a card"
	dealer.add_card(card)
	sleep(1.5)
	card = deck.draw_card()
	print user, "has drawn a {}".format(card)
	user.add_card(card)
	sleep(1.5)	
	card = deck.draw_card()
	print dealer, "has drawn a {}".format(card)
	dealer.add_card(card)
	sleep(1.5)
	user.print_hand()

def user_hit(user,deck):
	cont = True
	while cont:
		selection = str(raw_input("Enter if you would like to 'hit' or 'stay': "))
		sleep(1.5)		
		if selection == 'hit':
			card = deck.draw_card()
			user.add_card(card)
			print user, "has drawn a {}".format(card)
			sleep(1.5)
			user.print_hand()
		else:
			print "You have choosen to stay."
			cont = False 

def dealer_hit(dealer,deck):
	"""
	Dealer must play by the rules...
	Hit up to 17
	"""
	while dealer.handvalue < 17:
		card = deck.draw_card()
		dealer.add_card(card)
		print dealer, "has drawn a {}".format(card)
		sleep(1.5)
		dealer.print_hand()

def win_check(user,dealer):
	if user.handvalue > dealer.handvalue:
		

#def deal_card(user,deck):
#	card = deck.draw_card
#	user.add_card(card)
#	print user, "has drawn a {}".format(card) 


player1 = Player(10,'You')
dealer = Player(1000000) #Even casinos have a limit!
deck = Deck()

game_setup(player1,dealer,deck)
user_hit(player1,deck)
dealer_hit(dealer,deck)
