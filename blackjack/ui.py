# -*- coding: utf-8 -*-

class Texts(object):
    action_prompt = "Choose action: "
    round_actions = "(h)it, (s)tand, or (d)ouble? "
    n_player_prompt = "Choose number of players: "
    player_name_prompt = "Enter player name: "
    main_menu = """Blackjack - Main menu

    (n)ew game
    (o)ptions 
    (q)uit
    """
    
    new_game = """Starting a new game."""
    new_round = """New round."""
    next_round_prompt = """Play a new round? (y/n): """
    quit_message = """Quitting. Bye bye!"""
    busted = "Hand value over 21. Busted!"
    unknown_action = "Unknown action. Please retry. "

class Actions(object):
    round_actions = "hsd"
    main_menu_actions = "noq"

    # This seems like a tautology
    valid_round_actions = list(round_actions)
    valid_main_menu_actions = list(main_menu_actions)

def main_menu():
    print Texts.main_menu

    action = str(raw_input(Texts.action_prompt))
    return action

def round_menu(player, hand):
    print "Player", str(player) + "'s turn, hand #" + str(player.currentHand + 1) +" :", hand
    action = str(raw_input(Texts.action_prompt + Texts.round_actions))
    if action not in Actions.valid_round_actions:
        return round_menu(player, hand)
    else: 
        return action



def new_game():
    # might return list of players in future?
    return int(raw_input(Texts.n_player_prompt))

def get_players(nPlayers):
    players = []
    for i in xrange(nPlayers):
        players.append(str(raw_input(Texts.player_name_prompt)))
    return players

def play_next_round():
    answer = str(raw_input(Texts.next_round_prompt))
    if (answer == 'y'): return True
    if (answer == 'n'): return False
    else: return play_next_round()

def options():
    pass


def print_status(game):
    print "Status:"
    print "Dealer's hand:\t", game.dealer.handList[game.dealer.currentHand]
    print "Dealer's hand value:", game.dealer.handList[game.dealer.currentHand].value
    print
    for plr in game.players:
        i = 0
        print "Player", plr, "has", len(plr.handList), "hands"
        for hand in plr.handList:
            i += 1
            print "Player", plr, "hand #" + str(i), "is", hand
            print "With a value of", hand.value
            print
        print
    print
            



