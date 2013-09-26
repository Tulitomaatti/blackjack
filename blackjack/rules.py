# -*- coding: utf-8 -*-

class Rules(object):
    """Includes variables related to game rules.

    Rule variables:

    money_back_on_draw    - Whether money is returned on a draw.
    dealer_hand_min_value - Minimum value for dealer's hand.
    win_payout_factor     - How much of the original bet is won.
    win_blackjack_factor  - How much of the bet is won on a blackjack.
    hand_max_value        - Maximum hand value before the hand is
                            considered to be busted.

    """
    def __init__(self):
        self.money_back_on_draw = True
        self.dealer_hand_min_value = 17
        self.win_payout_factor = 1
        self.win_blackjack_factor = 1.5
        self.hand_max_value = 21
        self.number_of_packs = 4

    def __str__(self):
        # This could be also done by some fancy dir(obj) iterating but... yeah. 
        return '\n'.join(["Money back on draw: " + str(self.money_back_on_draw),
            "Dealer hand minimum value: "+ str(self.dealer_hand_min_value),
            "Win payout factor: " + str(self.win_payout_factor),
            "Blackjack win payout factor: "+ str(self.win_blackjack_factor),
            "Maximum hand value: "+ str(self.hand_max_value), 
            "Number of packs used: " + str(self.number_of_packs)])



    def value(hand):
        """Return hand value. """
        # First check for aces/soft hands

        # Otherwise just calculate value as usually. 
        pass