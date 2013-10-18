# -*- coding: utf-8 -*-
    
import random

# Maybe there is a better place for these
suits     = ["heart", "spade", "club", "diamond"]
numbers = range(1,14)

class Card(object):
    """A playing card that is defined by its number & suit"""

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        # I hear ''.join() is better somehow. 
        return str(self.number) + ' of ' + str(self.suit) + 's'

    def __eq__(self, other): 
        # Easier than always fetching numbers & suits
        return (self.number == other.number and self.suit == other.suit)

    def __ne__(self, other):
        return not self.__eq__


class Pack(object):
    """A pack of playing cards.

    Properties:
    card_stack - A list that includes the cards in the pack.

    Actions:
    shuffle()           - Shuffles the pack.
    put_card()           - Puts a card on top of the pack.
    draw_card([amount])  - Draws cards from the top.
    """

    def __init__(self):
        self.card_stack = []

    def shuffle(self):
        """Shuffles the pack."""
        random.shuffle(self.card_stack)

    def put_card(self, card):
        """Inserts a card to the top of the pack."""
        self.card_stack.append(card)

    def draw_card(self, amount=1):
        """Returns the topmost card of the pack. If many cards are
        requested, a list of the topmost cards is returned. 
        If the pack runs out of cards, the discard_stack is shuffled
        and used as a new pack. 

        """
        # card_stack[0] is the bottom of the pack,
        # card_stack.pop() should return the topmost card.

        if (amount == 1):
        # Would be nice to handle IndexError here but that'd 
        # require handing game objects to here which sounds silly.
            card = self.card_stack.pop()
            return card

        else: 
            # things that call this with amount > 1 have to be able to accept lists?
            cardList = []
            for i in xrange(amount):
                cardList.append(self.card_stack.pop())
            return cardList


    def __len__(self): 
        return len(self.card_stack)

    def __eq__(self, other):
        if (len(self) != len(other)): 
            return False

        elif (len(self) == 0 and len(other) == 0):
            return True

        else:
            for i in xrange(len(self)):
                if (self.card_stack[i] != other.card_stack[i]):
                    return False

        return True


class Hand(Pack):
    """A hand of cards. Has a bet and game-related attributes."""

    def __init__(self):
        """Hands are initialized empty with zero bet."""
        self.card_stack = []

        self.bet = 0.0
        self.final_hand = False
        self.blackjack_hand = False

    def double_bet(self):
        """Doubles the bet of the hand."""
        self.bet *= 2

    def __str__(self):
        """Returns a string representation of the hand."""

        # TODO : reimplement with .join()
        hand_string = ''
        for card in self.card_stack:
            if (hand_string == ''):
                hand_string += str(card)
            else:
                hand_string += ', ' + str(card)

        return hand_string

    # The decision to move value of a hand to be handles by rules 
    # was silly on retrospect. We could've had the value be calculated here,
    # and maybe just consult rules while doing so. 



