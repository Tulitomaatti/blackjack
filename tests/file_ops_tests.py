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

class Foo(object):
    pass

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
    try: 
        os.remove('players.bj')
    except Exception:
        pass
    try: 
        os.remove('rules.bj')
    except Exception:
        pass
    try: 
        os.remove('stats.bj')
    except Exception:
        pass


# read_it and save_it
def test_helpers():
    try:
        os.remove("it.bj")
    except IOError:
        pass
        
    a = Foo()
    a.name = 'foo'
    a.value = 45.5

    fop.save_it(a, 'it')

    b = fop.read_it('it')

    assert_true(a.name == b.name and a.value == b.value)

    os.remove("it.bj")

# Reading and saving a player

def test_single_player_wr():
    remove_bj_files()

    o, p, r = create_stuff()

    fop.save_player(o)

    players = fop.read_players()

    s = players[0]

    assert_equal(o.balance, s.balance)
    assert_equal(o.name, s.name)
    assert_equal(o.hand_list, [])
    assert_equal(o.current_hand, 0)

    remove_bj_files()

def test_many_player_wr():
    remove_bj_files()

    o, p, r = create_stuff()
    players = [o, p]

    for plr in players:
        fop.save_player(plr)

    plrs_in_file = fop.read_players()

    assert_true(len(plrs_in_file) == 2)

    x = plrs_in_file[0]
    y = plrs_in_file[1]

    assert_true(x.name == o.name and y.name == p.name and 
                x.balance == o.balance and y.balance == p.balance)

    remove_bj_files()

def test_rules_wr():
    remove_bj_files()

    o, p, r = create_stuff()

    r.dealer_hand_min_value = 16

    fop.save_rules(r)

    s = fop.read_rules()

    assert_equal(str(s),str(r))

    k = Rules()

    assert_not_equal(k.dealer_hand_min_value, s.dealer_hand_min_value)

    remove_bj_files()



# def test_game_stats

# Reading and saving game stats
