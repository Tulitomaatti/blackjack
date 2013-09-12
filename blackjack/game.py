# -*- coding: utf-8 -*-

import cardpackhand as c
import player as p
import rules as r


class Game(object):
    """A game of blackjack. Has rules, a pack of cards, and players.

    Attributes:
    rules   - Rules for this game.
    pack    - The pack that is used to play.
    dealer  - The dealer player.
    players - A list of players participating

    Actions: 
    betting()       - Get bets from each player for this round.
    deal()          - Deal cards for this round.
    payout()        - Pay winnings.

    initPack()      - Create a standard 52 card pack of cards.
    shufflePack()   - Shuffles the pack. 

    """

    def __init__(self):

        self.rules = r.Rules()
        self.pack = c.Pack()
        self.discardStack = c.Pack()

        self.dealer = p.Player('Dealer')
       
        self.players = []

    def betting(self):
        """Gets a bet from each player."""

        # Later on: implement a minimum bet.
        for player in self.players:
            player.handList.append(c.Hand())
            player.bet(float(raw_input("Enter bet: ")))

        print "Betting finished."

    def deal(self):
        """Deals two cards to each player and the dealer."""
        for i in xrange(2):
            print "Dealer draws a card."
            self.dealer.handList[0].putCard(self.pack.drawCard())

            for plr in self.players:
                print "Player", plr, "draws a card."
                plr.handList[plr.currentHand].putCard(
                    self.pack.drawCard())

    def payout(self):
        """Pays winnings to each player."""

           # Maybe create functions like bustedPayout() and blackjackPayout()? 

           # todo: have dealer collect lost bets.
        for player in self.players:
            for hand in player.handList:
                if (hand.blackjackHand):
                    player.balance += hand.bet
                    player.balance += hand.bet * self.rules.winBlackjackFactor
                    print "Player got blackjack and won", 

                elif (hand.bustedHand):
                    if (self.dealer.handList[self.dealer.currentHand].bustedHand and self.rules.moneyBackOnDraw):
                        player.balance += hand.bet
                        print "Busted, but so was the dealer. Bet returned."
                    else:
                        print "Hand was busted, no payout."

                elif (hand.value > self.dealer.handList[self.dealer.currentHand].value or 
                    self.dealer.handList[self.dealer.currentHand].bustedHand):
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
        """Shuffles the pack in play."""
        self.pack.shuffle()

    def discardCardsInPlay(self):
        for plr in self.players:
            for hand in plr.handList:
                for i in xrange(len(hand)):
                    self.discardStack.putCard(hand.drawCard())
                del hand

        for i in xrange(len(self.dealer.handList[self.dealer.currentHand])):
            self.discardStack.putCard(self.dealer.handList[self.dealer.currentHand].drawCard())

