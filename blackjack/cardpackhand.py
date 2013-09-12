# -*- coding: utf-8 -*-
    
import random

# Maybe there is a better place for these
suits     = ["heart", "spade", "club", "diamond"]
numbers = range(1,14)

class Card(object):
    """A playing card that is defined by its number & suit"""

    def __init__(self, number, suit):
        self.NUMBER = number
        self.SUIT = suit

    def __str__(self):
        # I hear ''.join() is better somehow. 
        return str(self.NUMBER) + ' of ' + str(self.SUIT) + 's'


class Pack(object):
    """A pack of playing cards.

    Properties:
    cardStack - A list that includes the cards in the pack.

    Actions:
    shuffle()           - Shuffles the pack.
    putCard()           - Puts a card on top of the pack.
    drawCard([amount])  - Draws cards from the top.

    printPack()         - Prints the cards in the pack.
    """

    def __init__(self):
        self.cardStack = []

    def shuffle(self):
        """Shuffles the pack."""
        random.shuffle(self.cardStack)

    def putCard(self, card):
        """Inserts a card to the top of the pack."""
        self.cardStack.append(card)

    def drawCard(self, amount=1):
        """Returns the topmost card of the pack. If many cards are
        requested, a list of the topmost cards is returned.

        """
        # cardStack[0] is the bottom of the pack,
        # cardStack.pop() should return the topmost card.
        if (amount == 1):
            card = self.cardStack.pop()

            print "Drew", card
            return card

        else: 
            # things that call this with amount > 1 have to be able to accept lists?
            print "Drawing", amount, "cards."
            cardList = []
            for i in xrange(amount):
                cardList.append(self.cardStack.pop())
            return cardList


    def __len__(self): 
        return len(self.cardStack)

    def printPack(self):
        """Prints all cards in the pack and states the number of
        cards."""

        for card in self.cardStack:
            print card
        print "A total of", len(self.cardStack), "cards."


class Hand(Pack):
    """A hand of cards. Has a bet and game-related attributes."""

    def __init__(self):
        """Hands are initialized empty with zero bet."""
        self.cardStack = []

        self.bet = 0.0
        self.finalHand = False
        self.bustedHand = False
        self.blackjackHand = False

    # This _seems_ to just work for some reason... suspicious.
    # I'd like to have the value inside __init__ rather. 
    @property
    def value(self):
        x = 0
        for i in xrange(len(self)):
            x += self.cardStack[i].NUMBER
        return x

    def doubleBet(self):
        """Doubles the bet of the hand."""
        self.bet *= 2

    def __str__(self):
        """Returns a string representation of the hand."""
        handString = ''
        for card in self.cardStack:
            if (handString == ''):
                handString += str(card)
            else:
                handString += ', ' + str(card)

        return handString



