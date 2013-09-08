# -*- coding: utf-8 -*-

import random

suits 	= ["heart", "spade", "club", "diamond"]
numbers = range(1,14)

class Card(object):
	"""A playing card defined by it's number & suit"""

	def __init__(self, number, suit):
		self.NUMBER = number
		self.SUIT = suit

	def __str__(self):
		return str(self.NUMBER) + ' of ' + str(self.SUIT) + 's'


class Pack(object):
	"""A pack of cards. Can be shuffled, and cards can be taken and added."""
	cardStack = []

	def shuffle(self):
		random.shuffle(self.cardStack)

	def putCard(self, card):
		self.cardStack.append(card)

	def drawCard(self, amount = 1):
		"""Returns the topmost card of the pack. If many cards are requested it returns a list of the topmost cards."""
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
				cardList.append(cardStack.pop())
			return cardList


	def __len__(self): return len(self.cardStack)

	def printPack(self):
		for card in self.cardStack:
			print card
		print "A total of", len(self.cardStack), "cards."


class Hand(Pack):
	"""A hand of cards. Tailored for blackjack."""

	bet = 0.0
	finalHand = False
	bustedHand = False
	blackjackHand = False

	def getValue(self):
		value = 0
		for i in xrange(len(self)):
			value += self.cardStack[i].NUMBER
		return value

	# Feels more elegant than always using some somehand.getHandValue() thing.
	value = property(getValue)

	def doubleBet(self):
		self.bet *= 2

	def __str__(self):
		handString = ''
		for card in self.cardStack:
			handString += ', ' + str(card)

		return handString




# sublime text had this nice autocomplete template, which i don't really understand (the **foo part)
	# def valueproperty():
	#     doc = "The foo property."
	#     def fget(self):
	#     	value = 0
	#     	for card in self.cardStack:
	#     		value += card.NUMBER
	#     	return value
	        
	#     def fset(self, value):
	#         print "Hand value cannot be set."
	#         return
	#     def fdel(self):
	#     	print "Hand value cannot be deleted."
	#         return
	#     return locals()
	# foo = property(**foo())


