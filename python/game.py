# -*- coding: utf-8 -*-

import cardpackhand as c
import player as p
import rules as r


class Game(object):
    rules = r.Rules()
    pack = c.Pack()

    dealer = p.Player()
    player = p.Player()    

    players = [player]

    def betting(self):
        for player in self.players:
            player.handList.append(c.Hand())
            player.bet(float(raw_input("Enter bet: ")))

        print "Betting finished."

    def deal(self):
        for i in xrange(2):
            print "Dealer draws a card."
            self.dealer.handList[0].putCard(self.pack.drawCard())

            for plr in self.players:
                print "Player", plr, "draws a card."
                plr.handList[plr.currentHand].putCard(self.pack.drawCard())

    def payout(self):    
        # Maybe create functions like bustedPayout() and blackjackPayout()? 
        for player in self.players:
            for hand in player.handList:
                if (hand.blackjackHand):
                    player.balance += hand.bet
                    player.balance += hand.bet * self.rules.winBlackjackFactor
                    print "Player got blackjack and won", 

                elif (hand.bustedHand):
                    if (self.dealer.handList[self.dealer.currentHand].bustedHand and r.moneyBackOnDraw):
                        player.balance += hand.bet
                        print "Busted, but so was the dealer. Bet returned."
                    else:
                        print "Hand was busted, no payout."

                elif (hand.value > self.dealer.handList[self.dealer.currentHand].value or self.dealer.handList[self.dealer.currentHand].bustedHand):
                    player.balance += hand.bet
                    player.balance += hand.bet*self.rules.winPayoutFactor
                    print "Hand won, got bet and", hand.bet*self.rules.winPayoutFactor

                else:
                    print "Hand lost to dealer."

        
    def initPack(self):
        print "Creating a standard 52 card pack."
        for suit in c.suits:
            for number in c.numbers:
                self.pack.putCard(c.Card(number, suit))
            
    def shufflePack(self):
        self.pack.shuffle()

