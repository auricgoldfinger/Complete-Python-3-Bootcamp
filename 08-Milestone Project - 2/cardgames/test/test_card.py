from game.card import Card
from game.suit import Suit
from game.rank import Rank
import unittest
class Card_Test(unittest.TestCase):

    def test_simple_card(self):
        suit = Suit.HEARTS
        rank = Rank.ACE
        my_card = Card(suit, rank)
        self.assertEqual(str(my_card), 'ACE of HEARTS')
        self.assertEqual(my_card.value(), 11)

if __name__ == '__main__':
    unittest.main()