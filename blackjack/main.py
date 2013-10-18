# -*- coding: utf-8 -*- 

import game as g
#import player as p
import rules as r
import file_ops as f
import ui
from ui import Texts as msg

#import pdb

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

    game.create_players()

    play_next_round = True

    while (play_next_round):
        game.play_round()
        # players are saved at the end of each round in game.py

        play_next_round = ui.play_next_round()


def options():
    action = ui.options()
    if (action == 'r'):
        print r.Rules()
    elif (action == 's'):
        players = f.read_players()

        for plr in players:
            print "Stats for", plr
            plr.stats.print_stats()
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

