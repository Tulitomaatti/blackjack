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

# TODO : Split some tests (easier problem pinpointing.)

def test_card():
    card1, card2, card3 = create_some_cards()


    # Same valued cards have same values and suits. 
    assert_equal((card1.number, card1.suit), (card3.number, card3.suit))
    assert_not_equal((card1.number, card1.suit), (card2.number, card2.suit))

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
    assert_raises(IndexError, pack.draw_card)
   
    # Putting cards to a pack
    pack.put_card(card1)
    assert_equal(len(pack), 1)

    pack.put_card(card2)
    assert_equal(len(pack), 2)

    # If we draw a card it should be the same card we just put in.
    assert_equal(pack.draw_card(), card2)

    # Only one card should remain
    assert_equal(len(pack), 1)

    pack.put_card(card1)
    pack.put_card(card2)
    pack.put_card(card3)

    # Drawing cards from a pack
    cards = pack.draw_card(3)

    # Cards come out of the pack in the reverse order we put them in.
    assert_equal(cards, [card3, card2, card1])

def test_pack_shuffling():
    a = Pack()
    b = Pack()

    # init_pack(a)
    # init_pack(b)

    # Something fishy around here. This should fail as it is. 
    # Have to inspect __eq__ in pack and card.
    card = Card(1,'a')

    a.put_card(card)
    b.put_card(card)

    assert_true(a == b)

    shuffle_pack(a)

    assert_true(a == b)

    # Shuffling a pack should (usually) give a differently ordered aepack

def test_hand():
    h = Hand()
    card1, card2, card3 = create_some_cards()

    # Set a bet for a hand.
    h.bet = 10

    assert_equal(h.bet, 10)

    h.put_card(card1)
    h.put_card(card2)
    h.put_card(card3)

    card_value_sum = 0 
    for i in xrange(len(h)):
        if h.card_stack[i].number > 10:
            card_value_sum += 10
        else:
            card_value_sum += h.card_stack[i].number

    assert_equal(h.value, card_value_sum)

    # Hand not busted yet, 1+k+1 = 12
    assert_false(h.busted)

    h.put_card(card2)

    # hands get busted after one more King( 12 + 10 = 22)
    assert_true(h.busted)


def test_hand_negative_bet():
    h = Hand()
    # This should fail at the moment since nothing is done to ensure positive bets.
    assert_raises(Exception, set_negative_bet, h)


def test_hand_bet_doubling():
    h = Hand()
    bet = 10
    h.bet = bet
    h.double_bet()

    assert_equal(h.bet, bet*2)

def create_some_cards():
    return Card(1, 'spade'), Card(13, 'hearts'), Card(1, 'spade')

def init_pack(pack):
    """Add the standard 52 cards to the pack"""
    for suit in suits:
       for number in numbers:
           pack.put_card(Card(number, suit))
    
def shuffle_pack(pack):
    """Shuffles the pack"""
    pack.shuffle()

def set_negative_bet(hand):
    hand.bet = -30
