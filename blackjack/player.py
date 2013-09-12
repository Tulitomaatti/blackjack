# -*- coding: utf-8 -*-
import cardpackhand

class Player(object):
    """Represents a player, includes actions that a player may take.

    Player attributes:
    name 		- Player name
    balance		- How much money the player has.
    handList	- A list of hands the player has.
    currentHand - Which hand is being handled at the moment.

    Player actions:
    bet 		- Place a bet for a hand.
    stand 		- End playing this hand. 
    hit 		- Request one card from the dealer. 
    double		- Double the bet, and receive only _one_ more card.
    split		- Split the hand in two. NOT IMPLEMENTED
    insurance	- Buy insurance for dealer's blackjack. NOT IMPLEMENTED

    printCurrentHand() Will print the current hand.

    """

    def __init__(self, name):
    	"""Players are initialized with zero balance and an empty hand."""
    	self.name = name
        self.balance = 0.0
        self.handList = []
        self.handList.append(cardpackhand.Hand())
        self.currentHand = 0

    def bet(self, bet, handIndex = 0):
    	"""Places a bet on a hand owned. Bet is reduced from balance."""
        self.balance -= bet
        self.handList[self.currentHand].bet += bet

        print "Bet", bet

    def stand(self, hand):
    	"""Finish playing this hand for this round."""
        hand.finalHand = True

        print "Standing."

    def hit(self, pack):
    	"""Request a card from the dealer."""
        print "Hitting a card:",
        self.handList[self.currentHand].putCard(pack.drawCard())

    def double(self, pack):
    	"""Get one final card from the dealer and double the hand's bet."""
        self.bet(self.handList[self.currentHand].bet)
        self.handList[self.currentHand].putCard(pack.drawCard())
        self.handList[self.currentHand].finalHand = True
        

    def split(self):
    	"""Split hand in two when initial cards have the same number."""
        pass

    def insurance(self):
    	"""Buy insurance when it looks like the dealer gets a blackjack."""
        pass

    def printCurrentHand(self):
    	"""Print the current hand."""
        print self.handList[self.currentHand]

class HumanPlayer(Player):
    pass

class AIPlayer(Player):
    pass
