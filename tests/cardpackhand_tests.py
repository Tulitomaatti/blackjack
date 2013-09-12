from nose.tools import *
from blackjack.cardpackhand import Card
from blackjack.cardpackhand import Pack
from blackjack.cardpackhand import Hand
from blackjack.cardpackhand import suits
from blackjack.cardpackhand import numbers


# def setup(): 
#     pass

# def teardown():
#     pass

# def test_basic():
#     print "testing..."


# @with_setup(setup, teardown)
# def test_with_setup_and_teardown():
#     pass

def test_card():
    card1, card2, card3 = create_some_cards()


    # Same valued cards have same values and suits. 
    assert_equal((card1.NUMBER, card1.SUIT), (card3.NUMBER, card3.SUIT))
    assert_not_equal((card1.NUMBER, card1.SUIT), (card2.NUMBER, card2.SUIT))

    # But two like cards are not the same card
    assert_is_not(card1, card2)

    # I suppose cards could have any number or a suit 'saxophone'.
    # Maybe test that in context of creating a standard pack. 

    # Create nonsensible card should fail.
    assert_raises(Exception, Card("dinosaur", -304.3))

def test_pack():
    pack = Pack()
    card1, card2, card3 = create_some_cards()

    # Empty packs are empty
    assert_equal(len(pack), 0)

    # Can't get cards from an empty pack
    assert_raises(IndexError, pack.drawCard)
   
    # Putting cards to a pack
    pack.putCard(card1)
    assert_equal(len(pack), 1)

    pack.putCard(card2)
    assert_equal(len(pack), 2)

    # If we draw a card it should be the same card we just put in.
    assert_equal(pack.drawCard(), card2)

    # Only one card should remain
    assert_equal(len(pack), 1)

    pack.putCard(card1)
    pack.putCard(card2)
    pack.putCard(card3)

    # Drawing cards from a pack
    cards = pack.drawCard(3)

    # Cards come out of the pack in the reverse order we put them in.
    assert_equal(cards, [card3, card2, card1])

def test_pack_shuffling():
    a = Pack()
    b = Pack()

    # initPack(a)
    # initPack(b)

    # Something fishy around here. This should fail as it is. 
    # Have to inspect __eq__ in pack and card.
    card = Card(1,'a')

    a.putCard(card)
    b.putCard(card)

    assert_true(a == b)

    shufflePack(a)

    assert_true(a == b)

    # Shuffling a pack should (usually) give a differently ordered aepack

def test_hand():
    h = Hand()
    card1, card2, card3 = create_some_cards()

    # Set a bet for a hand.
    h.bet = 10

    assert_equal(h.bet, 10)

    h.putCard(card1)
    h.putCard(card2)
    h.putCard(card3)

    card_value_sum = 0 
    for i in xrange(len(h)):
        if h.cardStack[i].NUMBER > 10:
            card_value_sum += 10
        else:
            card_value_sum += h.cardStack[i].NUMBER

    assert_equal(h.value, card_value_sum)

    # Hand not busted yet, 1+k+1 = 12
    assert_false(h.bustedHand)

    h.putCard(card2)

    # hands get busted after one more King( 12 + 10 = 22)
    assert_true(h.bustedHand)


def test_hand_negative_bet():
    h = Hand()
    # This should fail at the moment since nothing is done to ensure positive bets.
    assert_raises(Exception, set_negative_bet, h)


def test_hand_bet_doubling():
    h = Hand()
    bet = 10
    h.bet = bet
    h.doubleBet()

    assert_equal(h.bet, bet*2)

def create_some_cards():
    return Card(1, 'spade'), Card(13, 'hearts'), Card(1, 'spade')

def initPack(pack):
    """Add the standard 52 cards to the pack"""
    for suit in suits:
       for number in numbers:
           pack.putCard(Card(number, suit))
    
def shufflePack(pack):
    """Shuffles the pack"""
    pack.shuffle()

def set_negative_bet(hand):
    hand.bet = -30
