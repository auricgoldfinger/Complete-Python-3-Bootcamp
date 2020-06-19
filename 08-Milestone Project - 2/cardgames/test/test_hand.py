from game.hand import Hand
from game.card import Card
from game.rank import Rank
from game.suit import Suit
from blackjack.utils import BlackjackUtils
import unittest

class Test_Hand(unittest.TestCase):

    def test_simple_hand(self):
        my_hand = Hand(BlackjackUtils.calculate_value)

        self.assertEqual(0, my_hand.value())

        my_hand.add_card(Card(suit=Suit.HEARTS, rank=Rank.ACE))
        self.assertEqual(11, my_hand.value())

        my_hand.add_card(Card(suit=Suit.DIAMONDS, rank=Rank.TWO))
        self.assertEqual(13, my_hand.value())

        my_hand.add_card(Card(suit=Suit.SPADES, rank=Rank.QUEEN))
        # Expect ace to become value 1
        self.assertEqual(13, my_hand.value())

    def Test_Multiple_Aces(self):
        my_hand = Hand(BlackjackUtils.calculate_value)
        my_hand.add_card(Card(suit=Suit.HEARTS, rank=Rank.ACE))
        self.assertEqual(11, my_hand.value())

        my_hand.add_card(Card(rank=Rank.ACE, suit=Suit.CLUBS))
        self.assertEqual(12, my_hand.value())

        my_hand.add_card(Card(rank=Rank.ACE, suit=Suit.DIAMONDS))
        self.assertEqual(13, my_hand.value())

        my_hand.add_card(Card(rank=Rank.NINE, suit=Suit.HEARTS))
        self.assertEqual(12, my_hand.value())

if __name__ == "__main__":
    unittest.main()