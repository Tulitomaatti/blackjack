# -*- coding: utf-8 -*-

import cardpackhand as c
import player 		as p
import rules 		as r


class Game(object):
	rules 	= r.Rules()
	pack 	= c.Pack()

	dealer 	= p.Player()
	player 	= p.Player()	

	players = [player]


	def betting(self):
		for player in self.players:
			player.handList.append(c.Hand())
			player.bet(float(raw_input("Enter bet:")))

	def deal(self):
		for i in xrange(2):
			self.dealer.handList[self.dealer.currentHand].putCard(self.pack.drawCard())
			for player in self.players:
				player.handList[player.currentHand].append(pack.drawCard())


		print self.dealer.handList[self.dealer.currentHand]
		for player in self.players:
			print player.handList[player.currentHand]


	def payout(self):	
		for player in self.players:
			for hand in player.handList:
				if (hand.blackjackHand):
					player.balance += bet
					player.balance += bet*rules.winBlackjackFactor
					print "Player got blackjack and won", bet*rules.winBlackjackFactor

				elif (hand.bustedHand):
					if (self.dealer.handList[self.dealer.currentHand].bustedHand and r.moneyBackOnDraw):
						player.balance += bet
						print "Busted, but so was the dealer. Bet returned."
					else:
						print "Hand was busted, no payout."

				elif (hand.value > self.dealer.handList[self.dealer.currentHand].value or self.dealer.handList[self.dealer.currentHand].bustedHand):
					player.balance += bet
					player.balance += bet*rules.winPayoutFactor
					print "Hand won, got bet and", bet*rules.winPayoutFactor

				else:
					print "Hand lost to dealer."

		
	def initPack(self):
		print "Creating a standard 52 card pack."
		for suit in c.suits:
			for number in c.numbers:
				self.pack.putCard(c.Card(number, suit))
				self.pack.shuffle()
	