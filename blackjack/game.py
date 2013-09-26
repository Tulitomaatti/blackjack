# -*- coding: utf-8 -*-

import cardpackhand as c
import player as p
import rules as r
import ui


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
        self.discard_pack = c.Pack()

        self.dealer = p.Player('Dealer')
        self.dealer.hand_list.append(c.Hand())
       
        self.players = []



    def betting(self):
        """Gets a bet from each player."""

        # Later on: implement a minimum bet.
        for player in self.players:
            # Maybe empty hands should be created before the betting function is called?
            player.hand_list.append(c.Hand())


            # bet = ui.get_bet_from_player
            # check negative or minimum bet here? 
            bet = -1.0
            while (bet < 0):
                bet = ui.get_bet(player)

            player.bet(bet)


    def deal(self):
        """Deals two cards to each player and the dealer."""
        for i in xrange(2):
            card = None
            try:
                card = self.pack.draw_card()
            
            except IndexError:
                self._shuffle_discard_pile_and_use_as_current_pack()
                card = self.pack.draw_card()

            finally:
                self.dealer.hand_list[self.dealer.current_hand].put_card(card)


            card = None
            for plr in self.players:
                try: 
                    card = self.pack.draw_card()

                except IndexError:
                    self._shuffle_discard_pile_and_use_as_current_pack()
                    card = self.pack.draw_card()

                finally:
                    plr.hand_list[plr.current_hand].put_card(card)

    def payout(self):
        """Pays winnings to each player."""

       # Maybe create functions like bustedPayout() and blackjackPayout()? 
       # todo: have dealer collect lost bets.

        # For readability. 
        dealer_hand = self.dealer.hand_list[self.dealer.current_hand]

        for player in self.players:
            for hand in player.hand_list:
                if (hand.blackjack_hand):
                    # Draw doesn't get checked here, has to be moved.
                    player.balance += hand.bet
                    player.balance += hand.bet * self.rules.win_blackjack_factor

                elif (r.busted(hand)):
                    if (r.busted(dealer_hand) and self.rules.money_back_on_draw):
                        player.balance += hand.bet
                    else:
                        # Give the bet to the dealer. 
                        self.dealer.balance += hand.bet

                elif (r.value(hand) > r.value(dealer_hand) or
                      r.busted(dealer_hand)):

                    player.balance += hand.bet
                    player.balance += hand.bet*self.rules.win_payout_factor

                elif (r.value(hand) == r.value(dealer_hand) and
                      self.rules.money_back_on_draw):
                    player.balance += hand.bet
                else:
                    #hand lost. no payout needed, because bets are already taken when betting.
                    pass
        
    def init_pack(self):
        """Generates the standard 52 cards and puts them in the pack in play."""
        for suit in c.suits:
            for number in c.numbers:
                self.pack.put_card(c.Card(number, suit))
            
    def shuffle_pack(self):
        """Shuffles the pack in play."""
        self.pack.shuffle()

    def discard_cards_in_play(self):
        """Discards all cards in all hands on all players and the dealer."""
        for plr in self.players:
            for hand in plr.hand_list:
                for i in xrange(len(hand)):
                    self.discard_pack.put_card(hand.draw_card())

        for i in xrange(len(self.dealer.hand_list[self.dealer.current_hand])):
            self.discard_pack.put_card(self.dealer.hand_list[self.dealer.current_hand].draw_card())

    def round_cleanup(self):
        for player in self.players:
            del player.hand_list
            player.hand_list = []
            player.current_hand = 0

    def _shuffle_discard_pile_and_use_as_current_pack(self):
        """Makes the cards in discard pile the current pack and shuffle it."""
        del self.pack
        self.pack = self.discard_pack
        del self.discard_pack
        self.discard_pack = c.Pack()
        self.shuffle_pack()

