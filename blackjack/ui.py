# -*- coding: utf-8 -*-

class Texts(object):
    actionPrompt = "Choose action: "
    nPlayerPrompt = "Choose number of players: "
    playerNamePrompt = "Enter player name: "
    mainmenu = """Blackjack - Main menu

    (n)ew game
    (o)ptions 
    (q)uit
    """
    
    newGame = """Starting a new game."""
    newRound = """New round."""
    nextRoundPrompt = """Play a new round? (y/n): """
    quitMessage = """Quitting. Bye bye!"""

def mainMenu():
    print Texts.mainmenu

    action = str(raw_input(Texts.actionPrompt))
    return action

def newGame():
    # might return list of players in future?
    return int(raw_input(Texts.nPlayerPrompt))

def getPlayers(nPlayers):
    players = []
    for i in xrange(nPlayers):
        players.append(str(raw_input(Texts.playerNamePrompt)))
    return players

def playNextRound():
    answer = str(raw_input(Texts.nextRoundPrompt))
    if (answer == 'y'): return True
    if (answer == 'n'): return False
    else: return playNextRound()

def options():
    pass