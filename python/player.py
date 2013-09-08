# -*- coding: utf-8 -*-
import cardpackhand

class Player(object):

	def __init__(self):
		self.balance = 0.0
		self.handList = []
		self.handList.append(cardpackhand.Hand())
		self.currentHand = 0

	def bet(self, bet, handIndex = 0):
		self.balance -= bet
		self.handList[self.currentHand].bet += bet

		print "Bet", bet

	def stand(self, hand):
		hand.finalHand = True

		print "Standing."

	def hit(self, pack):
		print "Hitting a card:",
		self.handList[self.currentHand].putCard(pack.drawCard())

	def double(self, pack):
		self.bet(self.handList[self.currentHand].bet)
		self.handList[self.currentHand].putCard(pack.drawCard())
		self.handList[self.currentHand].finalHand = True
		

	def split(self):
		pass

	def insurance(self):
		pass

	def printCurrentHand(self):
		print self.handList[self.currentHand]

class HumanPlayer(Player):
	pass

class AIPlayer(Player):
	pass
