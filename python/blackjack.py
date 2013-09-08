# -*- coding: utf-8 -*- 

import game as g


if __name__ == "__main__":
	print "New game."

	game = g.Game()

	game.initPack()
	game.betting()
	game.deal()

	# check for blackjack

	for player in game.players:

		while (not player.handList[0].finalHand):
			print "Dealer has", game.dealer.handList[0]
			print "Your hand is", player.handList[game.player.currentHand]

			invalidAction = False
			while (invalidAction): 
				action = raw_input("Choose action: (h, s, d):")

				if (action == "h"):
					game.player.hit()
				elif (action == "d"):
					game.player.double()
				elif (action == "s"):
					game.player.stand()
				else:
					print "Unknown action."




