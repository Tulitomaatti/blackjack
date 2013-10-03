# -*- coding: utf-8 -*-
import rules as r
import player as p
import file_ops as fops

class Texts(object):
    action_prompt = "Choose action: "
    round_actions = "(h)it, (s)tand, or (d)ouble? "
    n_player_prompt = "Choose number of players: "
    player_name_prompt = "Enter player name: "
    please_select_players = "Please select players for the game."
    player_not_found = "Player not found."
    create_new_player_prompt = "Create new player with the name? (y / n)"
    player_already_selected = "Player has already been selected."
    remove_player_from_selection = "Remove player from selection? (y / n)"
    more_players_prompt = "Add more players? (y / n)"

    new_game = """Starting a new game."""
    new_round = """New round."""
    next_round_prompt = """Play a new round? (y/n): """
    quit_message = """Quitting. Bye bye!"""
    busted = "Hand value over 21. Busted!"
    unknown_action = "Unknown action. Please retry. "

    # Menu texts here
    main_menu = """Blackjack - Main menu

    (n)ew game
    (o)ptions 
    (q)uit
    """

    options_menu = """Blackjack - Options

    show (r)ules
    """
    

class Actions(object):
    round_actions = "hsd"
    main_menu_actions = "noq"
    option_actions = "r"

    # This seems like a tautology
    valid_round_actions = list(round_actions)
    valid_main_menu_actions = list(main_menu_actions)
    valid_option_actions = list(option_actions)

def main_menu():
    print Texts.main_menu

    action = str(raw_input(Texts.action_prompt))
    return action

def round_menu(player, hand):
    print "Player", str(player) + "'s turn, hand #" + str(player.current_hand + 1) +": value:", r.value(player.hand_list[player.current_hand])
    print hand
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


def get_players_for_game(players):
    selected = []
    n = 0

    print Texts.please_select_players


    # caution: bad code incoming: hard to read nesting & too long method

    action = ''
    while (action != 'n' and n < 5):
        name = str(raw_input(Texts.player_name_prompt))

        # there has to be a better way to do this: 

        # Find the player we requested.
        for player in players:
            if player.name == name:

                # Check if the player is already selected 
                for selected_player in selected:
                    if selected_player.name == name:
                        print Texts.player_already_selected
                        action = str(raw_input(Texts.remove_player_from_selection))

                        if action == 'y':
                            # Remove player from selection
                            # selected[] would create a new list. [:] assigns in place.
                            selected[:] = [plr for plr in selected if not plr.name == name]
                            action = ''
                            n -= 1
                        else: action = ''

                # Otherwise just append the player
                selected.append(player)
                n += 1

        # If no player was added, maybe create one?
        if len(selected) != n + 1:
            print Texts.player_not_found
            action = str(raw_input(Texts.player_name_prompt))
            if action == 'y':
                new_player = p.Player(name)
                players.append(new_player)
                fops.save_players(players)

                selected.append(new_player)
                n += 1
            else: action = ''

        while (action != 'y' and action != 'n'):
            action = str(raw_input(Texts.more_players_prompt))

    return selected




def play_next_round():
    answer = str(raw_input(Texts.next_round_prompt))
    if (answer == 'y'): return True
    if (answer == 'n'): return False
    else: return play_next_round()

def options():
    print Texts.options_menu
    action = str(raw_input(Texts.action_prompt))
    if action not in Actions.valid_option_actions:
        return options()
    else:
        return action

def get_bet(player):
    bet = float(raw_input(player.name + ", Enter bet: "))

    # TODO something about negative bets here
    return bet

def print_status(game):
    print "Status:"
    print "Dealer's hand:\t", game.dealer.hand_list[game.dealer.current_hand]
    print "Dealer's hand value:", r.value(game.dealer.hand_list[game.dealer.current_hand])
    print
    for plr in game.players:
        i = 0
        print plr, "balance:", plr.balance, 
        print plr, "has", len(plr.hand_list), "hands:"
        for hand in plr.hand_list:
            i += 1
            print "Player", plr, "hand #" + str(i), "is", hand
            print "With a value of", r.value(hand)
            print
        print
    print

def print_players(game):
    for plr in game.players:
        print plr.name, "balance: ", plr.balance
    print

def print_pack(pack):
    """Prints all cards in the pack and states the number of
    cards."""

    for card in pack.card_stack:
        print card
    print "A total of", len(pack.card_stack), "cards."
        



