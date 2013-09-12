# -*- coding: utf-8 -*- 

import pdb

import game as g
import player as p
import ui
from ui import Texts as msg


def createPlayers(game, nPlayers):
    players = ui.getPlayers(nPlayers)
    for i in xrange(nPlayers):
        game.players.append(p.Player(players[i]))
    return

def playRound(game):
#    pdb trace
    # Debug results:
    # * Pack has been created and shuffled
    # * Dealer and player have been created, both with an 
    #   empty handList. 


    game.betting()

  #  psdb.set_trace()

#    pdb trace
    # Debug results:
    #  * Player now has an empty hand in handList with a bet.
    #  * Dealer also has an empty hand. 

    game.deal()

#pdb.set_trace()
    # Debug results: 
    # * Player now has two cards in one hand. 
    # * Dealer now has two cards in one hand. 



    for player in game.players:
        player.currentHand = 0
        for hand in player.handList:
            while (not (hand.bustedHand or hand.finalHand)):
                ui.printStatus(game)

                # Debug results: 
                # * Player now has two cards in one hand. 
                # * Dealer now has two cards in one hand. 

                action = ui.roundMenu(player, hand)

                if (action == 'h'):
                    player.hit(game.pack)

                elif (action == 'd'):
                    player.double(game.pack)

                elif (action == 's'):
                    player.stand(hand)

                else:
                    # ui.py should take care of never ending here.
                    print msg.unknownAction
            player.currentHand += 1


# """ 
# Debug results: 
# * player has one hand with two cards after standing. 
# * dealer has two cards. 

# """

    # Dealer plays
    while (game.dealer.handList[0].value < game.rules.dealerHandMinValue):
        game.dealer.hit(game.pack)
        ui.printStatus(game)



    game.payout()

    #bet has been returned, winnings paid. 

    game.discardCardsInPlay()

    game.roundCleanup()


    # Debug here:
    # Player has one, EMPTY hand. So does the dealer. 
    # Player's hand has zero bet. 

    return

def newGame():
    print msg.newGame

    nPlayers = ui.newGame()

    game = g.Game()

    # Let's try with more packs. 
    for i in xrange(game.rules.numberOfPacks):
        game.initPack()

    game.shufflePack()
    createPlayers(game, nPlayers)

    playNextRound = True

    while (playNextRound):
        playRound(game)
        playNextRound = ui.playNextRound()

    return

def options():
    ui.options()


if __name__ == "__main__":

    while (True):
        action = ui.mainMenu()

        if (action == 'q'):
            print msg.quitMessage
            break

        elif (action == 'n'):
            newGame()

        elif (action == 'o'):
            options()

