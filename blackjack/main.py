# -*- coding: utf-8 -*- 

import game as g
import player as p
import ui
from ui import Texts as msg


def create_players(game, nPlayers):
    players = ui.getPlayers(nPlayers)
    for i in xrange(nPlayers):
        game.players.append(p.Player(players[i]))
    return

def play_round(game):

    game.betting()
    game.deal()

    for player in game.players:
        player.currentHand = 0
        for hand in player.handList:
            while (not (hand.bustedHand or hand.finalHand)):

                ui.printStatus(game)
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

    # Dealer plays
    while (game.dealer.handList[0].value < game.rules.dealerHandMinValue):
        game.dealer.hit(game.pack)
        ui.printStatus(game)

    game.payout()

    game.discardCardsInPlay()
    game.roundCleanup()

    return

def new_game():
    print msg.new_game

    nPlayers = ui.new_game()

    game = g.Game()

    # Let's try with more packs. 
    for i in xrange(game.rules.numberOfPacks):
        game.initPack()

    game.shufflePack()
    create_players(game, nPlayers)

    playNextRound = True

    while (playNextRound):
        play_round(game)
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
            new_game()

        elif (action == 'o'):
            options()

