# -*- coding: utf-8 -*- 

import game as g
import player as p
import ui
from ui import Texts as msg


def create_players(game, n_players):
    players = ui.get_players(n_players)
    for i in xrange(n_players):
        game.players.append(p.Player(players[i]))
    return

def play_round(game):

    game.betting()
    game.deal()

    for player in game.players:
        player.current_hand = 0
        for hand in player.hand_list:
            while (not (hand.busted or hand.final_hand)):

                ui.print_status(game)
                action = ui.roundMenu(player, hand)

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
    while (game.dealer.hand_list[0].value < game.rules.dealer_hand_min_value):
        game.dealer.hit(game.pack)
        ui.print_status(game)

    game.payout()

    game.discard_cards_in_play()
    game.round_cleanup()

    return

def new_game():
    print msg.new_game

    n_players = ui.new_game()

    game = g.Game()

    # Let's try with more packs. 
    for i in xrange(game.rules.number_of_packs):
        game.init_pack()

    game.shuffle_pack()
    create_players(game, n_players)

    play_next_round = True

    while (play_next_round):
        play_round(game)
        play_next_round = ui.play_next_round()

    return

def options():
    ui.options()


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

