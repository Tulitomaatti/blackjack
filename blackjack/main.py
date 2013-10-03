# -*- coding: utf-8 -*- 

import game as g
import player as p
import rules as r
import ui
from ui import Texts as msg


# Redo player logic to read players from a list / UI 
def create_players(game, n_players):
    players = ui.get_players(n_players)

    # Check here if we have enough cards in play. 
    # For now just quit if more than 4 players D:

    for i in xrange(n_players):
        game.players.append(p.Player(players[i]))


# Should be moved to game.py ?
def play_round(game):

    game.betting()
    game.deal()

    for player in game.players:
        player.current_hand = 0
        for hand in player.hand_list:
            while (not (r.busted(hand, game.rules) or hand.final_hand)):

                ui.print_status(game)   
                
                action = ui.round_menu(player, hand)

                if (action == 'h'):
                    player.hit(game.pack)

                elif (action == 'd'):
                    player.double(game.pack)

                elif (action == 's'):
                    player.stand(hand)

                else:
                    # ui.py should take care of never ending here.
                    print msg.unknown_action

            player.current_hand += 1

    # Dealer plays
    while (r.value(game.dealer.hand_list[0]) < game.rules.dealer_hand_min_value):
        game.dealer.hit(game.pack)
        ui.print_status(game)

    game.payout()

    game.discard_cards_in_play()

    # Here until nicer UI. 
    ui.print_players(game)

    game.round_cleanup()

def new_game():
    print msg.new_game

    n_players = ui.new_game()


    # For now > 4. TODO : Check if we have enough cards coming to play.
    if (n_players > 4): raise Exception("Too many players.")
 

    game = g.Game()

    # Let's try with more packs. 
    for i in xrange(game.rules.number_of_packs):
        game.init_pack()

    game.shuffle_pack()
    create_players(game, n_players)

    play_next_round = True

    while (play_next_round):
        play_round(game)

        # TODO Here: save players and game stats. 

        play_next_round = ui.play_next_round()


def options():
    if (ui.options() == 'r'):
        print r.Rules()
    else:
        pass


if __name__ == "__main__":

    while (True):
        action = ui.main_menu()

        if (action == 'q'):
            print msg.quit_message
            break

        elif (action == 'n'):
            new_game()

        elif (action == 'o'):
            options()

