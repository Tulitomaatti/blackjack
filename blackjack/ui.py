# -*- coding: utf-8 -*-

class Texts(object):
    actionPrompt = "Choose action: "
    roundActions = "(h)it, (s)tand, or (d)ouble?"
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
    busted = "Hand value over 21. Busted!"
    unknownAction = "Unknown action. Please retry. "

class Actions(object):
    roundActions = "hsd"
    mainMenuActions = "noq"

    # This seems like a tautology
    validRoundActions = list(roundActions)
    validMainMenuActions = list(mainMenuActions)

def mainMenu():
    print Texts.mainmenu

    action = str(raw_input(Texts.actionPrompt))
    return action

def roundMenu(player, hand):
    print "Player", str(player) + "'s turn, hand #" + str(player.currentHand + 1) +" :", hand
    action = str(raw_input(Texts.actionPrompt + Texts.roundActions))
    if action not in Actions.validRoundActions:
        return roundMenu(player, hand)
    else: 
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


def printStatus(game):
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
            



