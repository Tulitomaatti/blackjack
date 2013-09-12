# -*- coding: utf-8 -*-

class Rules(object):
	def __init__(self):
		self.moneyBackOnDraw 		= True

        # High for testing, should be 21 on release.
		self.dealerHandMinValue 	= 37
        
		self.winPayoutFactor 		= 1
		self.winBlackjackFactor 	= 1.5
		self.handMaxValue 			= 21