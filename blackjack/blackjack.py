# -*- coding: utf-8 -*- 

#This file looks more like a main.py. 
import game as g

if __name__ == "__main__":
    print "New game."

    game = g.Game()

    game.initPack()
    game.shufflePack()
    game.pack.printPack()
    game.betting()
    game.deal()

    # check for blackjack
    # blackjackcheckmagickfunction()

# unelegant game loop and ui. to be moved to main.py or equivalent
    for player in game.players:

        while (not player.handList[0].finalHand):
            print "Dealer has: \t", game.dealer.handList[0]
            print "Your hand is:\t", player.handList[game.player.currentHand]

            invalidAction = False
            while (not invalidAction): 
                action = raw_input("Choose action: (h, s, d):")

                if (action == "h"):
                    game.player.hit(game.pack)
                elif (action == "d"):
                    game.player.double(game.pack)
                elif (action == "s"):
                    game.player.stand(game.player.handList[game.player.currentHand])
                else:
                    print "Unknown action."

                if (player.handList[0].finalHand): break


    #dealer plays
    print "Dealer plays..."

    print "Dealer hand value:", game.dealer.handList[0].value

    while (game.dealer.handList[0].value < game.rules.dealerHandMinValue):
        print "hand under", game.rules.dealerHandMinValue, "dealer hits: "
        game.dealer.hit(game.pack)

    print "Everyone has done playing..."
    print "Dealer has: \t", game.dealer.handList[0]
    print "that's", game.dealer.handList[0].value, "for the dealer."
    print "Your hand is:\t", player.handList[game.player.currentHand]
    print "that's", game.player.handList[0].value, "for the player."


    #compare hands
    print "Comparing hands..."
    game.payout()

    print "Paying money to winners, losers get nothing and draw's get money back."

    print "Final situation:"
    print "player balance: ", game.players[0].balance

    print "Game over."

