from nose.tools import *
from blackjack.player import Player
from blackjack.cardpackhand import Hand
from blackjack.cardpackhand import Pack
from cardpackhand_tests import initPack

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
    assert_equal(p.handList, [])
    assert_equal(p.name, 'Fooman')
    assert_equal(p.currentHand, 0)

def test_player_betting():
    p = Player('Fooman')
    h = Hand()

    p.handList.append(h)

    p.bet(10)

    # balance should now be -10 and bet of the hand 10. 

    assert_true(p.balance == -10 and h.bet == 10)

def test_player_hitting():
    p = Player('Fooman')
    h = Hand()
    pack = Pack()
    length = len(pack)
    
    initPack(pack)
    p.handList.append(h)

    p.hit(pack)

    assert_true(len(p.handList[0]) == 1 and len(pack) == 51)

    hit_20_cards(p, pack)

    # Should bust from hitting 20 cards. 
    assert_true(p.handList[0].bustedHand)


def test_player_doubling():
    pass

def test_player_standing():
    p = Player('Fooman')
    p.handList.append(Hand())

    p.stand(p.handList[0])

    assert_true(p.handList[0].finalHand)

def test_player_splitting():
    pass

def test_player_insurance():
    pass




def hit_20_cards(plr, pack):
    for i in xrange(20):
        plr.hit(pack)


 




