# -*- coding: utf-8 -*-
import cardpackhand

class Player(object):
    """Represents a player, includes actions that a player may take.

    Player attributes:
    name 		- Player name
    balance		- How much money the player has.
    hand_list	- A list of hands the player has.
    current_hand - Which hand is being handled at the moment.

    Player actions:
    bet 		- Place a bet for a hand.
    stand 		- End playing this hand. 
    hit 		- Request one card from the dealer. 
    double		- Double the bet, and receive only _one_ more card.
    split		- Split the hand in two. NOT IMPLEMENTED
    insurance	- Buy insurance for dealer's blackjack. NOT IMPLEMENTED

    print_current_hand() Will print the current hand.

    """

    def __init__(self, name):
    	"""Players are initialized with zero balance and an empty hand."""
    	self.name = name
        self.balance = 0.0
        self.hand_list = []
        self.current_hand = 0

    def __str__(self):
    	return self.name

    def bet(self, bet, handIndex=0):
    	"""Places a bet on a hand owned. Bet is reduced from balance."""
        # Should negative bets be prevented here, in game, or in ui? 
        self.balance -= bet
        self.hand_list[self.current_hand].bet += bet


    def stand(self, hand):
    	"""Finish playing this hand for this round."""
        hand.final_hand = True


    def hit(self, pack):
    	"""Request a card from the dealer."""
        self.hand_list[self.current_hand].put_card(pack.draw_card())

    def double(self, pack):
    	"""Get one final card from the dealer and double the hand's bet."""
        self.bet(self.hand_list[self.current_hand].bet)
        #self.hand_list[self.current_hand].put_card(pack.draw_card())
        self.hit(pack)
        self.hand_list[self.current_hand].final_hand = True
        

    def split(self):
    	"""Split hand in two when initial cards have the same number."""
        pass

    def insurance(self):
    	"""Buy insurance when it looks like the dealer gets a blackjack."""
        pass

    def print_current_hand(self):
    	"""Print the current hand."""
        print self.hand_list[self.current_hand]

class HumanPlayer(Player):
    pass

class AIPlayer(Player):
    pass
