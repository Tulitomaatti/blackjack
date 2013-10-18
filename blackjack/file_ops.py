# -*- coding: utf-8 -*-
import pickle
import sys

BLACKJACK_FILE_EXTENSION = '.bj'

def read_it(it):
    try:
        f = open(it + BLACKJACK_FILE_EXTENSION, "rb")
    except IOError:
        print "Could not open", it, "file for reading."
        print it, "was not read."
        print "Trying to create an empty", it
        return -1


    obj = pickle.load(f)
    f.close()

    return obj

def save_it(obj, it):
    """Save it to a file."""
    try:
        f = open(it + BLACKJACK_FILE_EXTENSION, "wb")
    except IOError():
        print "Could not open", it, "file for writing."
        print it, "not written and might be lost."

    pickle.dump(obj, f)
    f.close()


def read_players():
    """Reads a player list and returns it."""

    players = read_it('players')
    if players == -1:
        try:
            f = open('players' + BLACKJACK_FILE_EXTENSION, "wb")
            players = []
            pickle.dump(players, f)
            f.close()
            print "Created an empty players file."
            return players 

        except IOError:
            print "Could not create players file."
            print "Exiting."
            sys.abort()



    return players 


# These functions are defined for better readibility elsewhere.
# Otherwise read_it() and save_it() could be called. 
def save_game_stats(game):
    """Saves game stats to a file."""
    save_it(game.stats, 'stats')

def save_players(players):
    """Writes players (list) to a file. Players are stripped of all cards on saving."""

    # This might cause cards to disappear, 
    # but hands should be empty at this point anyways.
    for player in players:
        player.hand_list = []
        player.current_hand = 0

    save_it(players, 'players')

def save_rules(rules):
    """Saves rules to a file."""
    save_it(rules, 'rules')

def read_game_stats():
    """Reads game stats from a file."""
    return read_it('stats')

def read_rules():
    """Read rules from a file."""
    rules = read_it('rules')
    return rules



