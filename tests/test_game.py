from blackjack.game import *
import config


def test_getDeck():
    deck = getDeck()
    assert len(deck) == 52

    ranks = [str(i) for i in range(2, 11)]
    ranks += ['J', 'Q', 'K', 'A']
    result = getDeck()
    for rank, suit in result:
        assert rank in ranks
        assert suit in (config.HEARTS,
                        config.DIAMONDS,
                        config.SPADES,
                        config.CLUBS)


def test_getHandValue():
    hand = [('A', config.SPADES), ('10', config.HEARTS)]
    assert getHandValue(hand) == 21

    hand = [('A', config.SPADES), ('9', config.HEARTS)]
    assert getHandValue(hand) == 20

    hand = [('A', config.SPADES), ('A', config.HEARTS), ('9', config.CLUBS)]
    assert getHandValue(hand) == 21



def test_dealerMove():
    dealerHand = [('10', config.SPADES), ('6', config.HEARTS)]
    while getHandValue(dealerHand) < 17:
        dealerHand.append(('2', config.CLUBS))

    assert getHandValue(
        dealerHand) >= 17
