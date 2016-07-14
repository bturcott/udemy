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
	pass

brad = Player(10)
print brad.wins
print brad.losses
print brad.bankroll

