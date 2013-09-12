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
    """A pack of playing cards. Can be shuffled, and cards can be taken 
    and added."""

    def __init__(self):
        self.cardStack = []

    def shuffle(self):
        random.shuffle(self.cardStack)

    def putCard(self, card):
        self.cardStack.append(card)

    def drawCard(self, amount = 1):
        """Returns the topmost card of the pack. If many cards are requested asdf it returns a list of the topmost cards.

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


    def __len__(self): return len(self.cardStack)

    def printPack(self):
        for card in self.cardStack:
            print card
        print "A total of", len(self.cardStack), "cards."


class Hand(Pack):
    """A hand of cards. Tailored for blackjack."""

    def __init__(self):
        self.cardStack = []

        self.bet = 0.0
        self.finalHand = False
        self.bustedHand = False
        self.blackjackHand = False

    # This _seems_ to just work for some reason... suspicious.
    @property
    def value(self):
        x = 0
        for i in xrange(len(self)):
            x += self.cardStack[i].NUMBER
        return x

        # I'm having problems getting this working

        # def value():
        #     doc = "The value of the hand in blackjack."
        #     def fget(self):
        #         value = 0
        #               for i in xrange(len(self)):
        #             value += self.cardStack[i].NUMBER
        #         return value

        #     # Proper errors should be raised instead of return None
        #     def fset(self, value):
        #         print "Can't set hand value. Change cards for that."
        #         return None
        #     def fdel(self):
        #         print "Can't delete hand value. Delete cards for that."
        #         return None
        #     return locals()

        # value = property(**value())



    def doubleBet(self):
        self.bet *= 2

    def __str__(self):
        handString = ''
        for card in self.cardStack:
            if (handString == ''):
                handString += str(card)
            else:
                handString += ', ' + str(card)

        return handString



