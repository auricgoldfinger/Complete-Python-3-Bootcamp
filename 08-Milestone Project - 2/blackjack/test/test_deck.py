from game.card import Card
from game.suit import Suit
from game.rank import Rank
from game.deck import Deck
import unittest
class Test_Deck(unittest.TestCase):

    def test_new_deck(self):
        my_deck = Deck()
        self.assertEqual(len(my_deck), 52)
        print(my_deck)

if __name__ == '__main__':
    unittest.main()