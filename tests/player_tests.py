from nose.tools import *
from blackjack.player import Player
from blackjack.cardpackhand import Hand
from blackjack.cardpackhand import Pack
from cardpackhand_tests import init_pack

# def setup(): 
#     pass

# def teardown():
#     pass

# def test_basic():
#     print "testing..."

def test_player_init():
    p = Player('Fooman')

    # Players should init with 0 balance and an empty hand list.
    print p.balance
  
    assert_equal(p.balance, 0)
    assert_equal(p.hand_list, [])
    assert_equal(p.name, 'Fooman')
    assert_equal(p.current_hand, 0)

def test_player_betting():
    p = Player('Fooman')
    h = Hand()

    p.hand_list.append(h)

    p.bet(10)

    # balance should now be -10 and bet of the hand 10. 

    assert_true(p.balance == -10 and h.bet == 10)

def test_player_hitting():
    p = Player('Fooman')
    h = Hand()
    pack = Pack()
    length = len(pack)
    
    init_pack(pack)
    p.hand_list.append(h)

    p.hit(pack)

    assert_true(len(p.hand_list[0]) == 1 and len(pack) == 51)

    hit_20_cards(p, pack)

    # Should bust from hitting 20 cards. 
    assert_true(p.hand_list[0].busted)


def test_player_doubling():
    pass

def test_player_standing():
    p = Player('Fooman')
    p.hand_list.append(Hand())

    p.stand(p.hand_list[0])

    assert_true(p.hand_list[0].final_hand)

def test_player_splitting():
    pass

def test_player_insurance():
    pass




def hit_20_cards(plr, pack):
    for i in xrange(20):
        plr.hit(pack)


 




