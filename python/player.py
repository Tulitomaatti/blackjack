# -*- coding: utf-8 -*-
import cardpackhand

class Player(object):
	balance = 0.0
	handList = []
	currentHand = 0

	def bet(self, bet, handIndex = 0):
		self.balance -= bet
		self.handList[self.currentHand].bet = bet

		print "Bet", self.bet

	def stand(self, hand):
		hand.finalHand = True

		print "Standing."

	def hit(self, pack):
		print "Hitting a card:",
		self.handList[self.currentHand].append(pack.drawCard())

	def double(self):
		self.bet(self.handList[currentHand].bet)
		self.handList[self.currentHand].append(pack.drawCard())
		self.handList[self.currentHand].finalHand = True
		

	def split(self):
		pass

	def insurance(self):
		pass

class HumanPlayer(Player):
	pass

class AIPlayer(Player):
	pass
