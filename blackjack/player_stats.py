# -*- coding: utf-8 -*-

class PlayerStats(object):
    def __init__(self): 
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.busts = 0
        self.bjs = 0
        self.average_bet = 0
        self.cards_played = 0
        self.hands_played = 0
        self.times_doubled = 0

    def update_average_bet(self, bet):
        # This doesn't calculate correctly afaik. 
        games_played = self.wins+self.losses+self.draws
        self.average_bet = (self.average_bet*games_played + bet) / (games_played+1)
   
    # memo: 
    # maybe track amounts of each value got? or something other complex, like hand starting values. 
    # self.cardthing

    def print_stats(self):
        # There was a nice way to loop through all properties of an object.
        # ...which I can't remember. Something with __stuff__. 
        print "Wins:", self.wins
        print "Losses:", self.losses
        print "Draws:", self.draws
        print "Busts:", self.busts
        print "Blackjacks:", self.bjs
        print "Average bet:", self.average_bet
        print "Cards played:", self.cards_played
        print "Hands played:", self.hands_played
        print "Times doubled:", self.times_doubled
        print


