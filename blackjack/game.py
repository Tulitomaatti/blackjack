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

    init_pack()      - Create a standard 52 card pack of cards.
    shuffle_pack()   - Shuffles the pack. 

    """

    def __init__(self):

        self.rules = r.Rules()
        self.pack = c.Pack()
        self.discardPack = c.Pack()

        self.dealer = p.Player('Dealer')
        self.dealer.handList.append(c.Hand())
       
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

            card = None
            try:
                card = self.pack.drawCard()
            
            except IndexError:
                self._shuffle_discard_pile_and_use_as_current_pack()
                card = self.pack.drawCard()

            finally:
                self.dealer.handList[self.dealer.currentHand].putCard(card)


            card = None
            for plr in self.players:
                print "Player", plr, "draws a card."

                try: 
                    card = self.pack.drawCard()

                except IndexError:
                    self._shuffle_discard_pile_and_use_as_current_pack()
                    card = self.pack.drawCard()

                finally:
                    plr.handList[plr.currentHand].putCard(card)

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

                elif (hand.value == self.dealer.handList[self.dealer.currentHand].value and self.rules.moneyBackOnDraw):
                    print "Draw! Bet returned."
                    player.balance += hand.bet


                else:
                    print "Hand lost to dealer."

        
    def init_pack(self):
        print "Adding a standard 52 card pack to play."
        for suit in c.suits:
            for number in c.numbers:
                self.pack.putCard(c.Card(number, suit))
            
    def shuffle_pack(self):
        """Shuffles the pack in play."""
        self.pack.shuffle()

    def discard_cards_in_play(self):
        for plr in self.players:
            for hand in plr.handList:
                for i in xrange(len(hand)):
                    self.discardPack.putCard(hand.drawCard())

        for i in xrange(len(self.dealer.handList[self.dealer.currentHand])):
            self.discardPack.putCard(self.dealer.handList[self.dealer.currentHand].drawCard())

    def round_cleanup(self):
        for player in self.players:
            del player.handList
            player.handList = []
            player.currentHand = 0

    def _shuffle_discard_pile_and_use_as_current_pack(self):
        print "Ran out of cards! Shuffling the discarded cards."
        del self.pack
        self.pack = self.discardPack
        del self.discardPack
        self.discardPack = c.Pack()
        self.shuffle_pack()

