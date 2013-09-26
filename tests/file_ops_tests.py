# -*- coding: utf-8 -*-

import os
from nose.tools import *
from blackjack.cardpackhand import Card
from blackjack.cardpackhand import Pack
from blackjack.cardpackhand import Hand
from blackjack.player import Player
from blackjack.game import Game
from blackjack.rules import Rules
import blackjack.file_ops as fop

def create_stuff(): 
    o = Player('Barman')
    o.balance = 200
    o.hand_list.append(Hand())
    o.hand_list[o.current_hand].put_card(Card(2,'heart'))

    p = Player('Fooman')
    p.balance = 150
    p.hand_list.append(Hand())
    p.hand_list[p.current_hand].put_card(Card(1,'spade'))

#   Stats not yet implemented.
#   q = Game()

    r = Rules()

    return o, p, r

def remove_bj_files():
    os.remove('players.bj')
    os.remove('rules.bj')
    os.remove('stats.bj')


def test_single_player_wr():
    o, p, r = create_stuff()

    fop.save_player(o)

    players = fop.read_players()

    s = players[0]

    assert_equal(o.balance, s.balance)
    assert_equal(o.name, s.name)


# Reading and saving a player

# Reading and saving rules

# Reading and saving game stats
