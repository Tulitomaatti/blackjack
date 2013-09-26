# -*- coding: utf-8 -*-
import pickle

BLACKJACK_FILE_EXTENSION = '.bj'

def read_it(it):
    try:
        f = open(it + BLACKJACK_FILE_EXTENSION, "rb")
    except IOError():
        print "Could not open", it, "file for reading."
        print it, "was not read."

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

    pickle.dump(it, f)
    f.close()

# This one is different. I couldn't figure out a nice way to read a single
# player by name from a pickled file, so better just read all of them. 
def read_players():
    """Reads a player list and returns it."""

    try:
        f = open('players' + BLACKJACK_FILE_EXTENSION, "rb")
    except IOError(): 
        print "Could not open players file for reading."
        print "Players were not read."
        return 
    
    players = []

    while(True):
        try:
            players.append(pickle.load(f))
        except EOFError():
            break

    f.close()
    return players 


# These functions are defined for better readibility elsewhere.
# Otherwise read_it() and save_it() could be called. 
def save_game_stats(game):
    """Saves game stats to a file."""
    save_it(game.stats, 'stats')

def save_player(player):
    """Appends player info to a file. Player is stripped of all cards on saving."""
    player.hand_list = []
    player.current_hand = 0
    save_it(player, 'players')

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



