# -*- coding: utf-8 -*- 

#This file looks more like a main.py. 
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
    game.betting()
    game.deal()


    for player in game.players:
        for hand in player.handList:
            while (not hand.finalHand):
                ui.printStatus(game)


                while (not hand.bustedHand and not hand.finalHand):
                    ui.printStatus(game)
                    action = ui.roundMenu()

                    if (action == 'h'):
                        player.hit(game.pack)
                        if (hand.bustedHand):
                            hand.finalHand = True
                            print msg.busted
                            break

                    elif (action == 'd'):
                        player.double(game.pack)

                    elif (action == 's'):
                        player.stand(hand)

                    else:
                        # ui.py should take care of never ending here.
                        print msg.unknownAction

                    if (hand.finalHand): break

    # Dealer plays
    while (game.dealer.handList[0].value < game.rules.dealerHandMinValue):
        game.dealer.hit(game.pack)
        ui.printStatus(game)

    game.payout()

    game.discardCardsInPlay()

    return

def newGame():
    print msg.newGame

    nPlayers = ui.newGame()

    game = g.Game()

    game.initPack()
    game.shufflePack()
#    game.pack.printPack()
    
    # get players for this game
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

