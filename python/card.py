# -*- coding: utf-8 -*-

class Card(object):
	final int NUMBER
	final string SUIT

	def __init__(self, number, suit):
		self.NUMBER = number
		self.suit = suit