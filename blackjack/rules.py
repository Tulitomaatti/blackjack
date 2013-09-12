# -*- coding: utf-8 -*-

class Rules(object):
    """Includes variables related to game rules.

    Rule variables:

    moneyBackOnDraw     - Whether money is returned on a draw.
    dealerHandMinValue  - Minimum value for dealer's hand.
    winPayoutFactor     - How much of the original bet is won.
    winBlackjackFactor  - How much of the bet is won on a blackjack.
    handMaxValue        - Maximum hand value before the hand is
                          considered to be busted.
                          
    """
    def __init__(self):
        self.moneyBackOnDraw = True

        # High for testing, should be 21 on release.
        self.dealerHandMinValue = 37

        self.winPayoutFactor = 1
        self.winBlackjackFactor = 1.5
        self.handMaxValue = 21