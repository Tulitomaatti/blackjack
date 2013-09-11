# -*- coding: utf-8 -*-

import random

# Maybe there is a better place for these
suits 	= ["heart", "spade", "club", "diamond"]
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


#adsfadfsdsafölkd afsasdflkj aölsdkfj öalsdkfj öalksdjf öalkdsjf loooong line longcat alsdkfjaöldkfjaödflkja kekkonen yeahhhhh lolz


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
		self.value = property(self.getValue)

	def getValue(self):
		value = 0
		for i in xrange(len(self)):
			value += self.cardStack[i].NUMBER
		return value

	# Feels more elegant than always using some somehand.getHandValue() thing.
	

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


