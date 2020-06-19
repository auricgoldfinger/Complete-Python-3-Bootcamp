from game.card import Card
from game.suit import Suit
from game.rank import Rank
from game.deck import Deck
import unittest
class Test_Deck(unittest.TestCase):

    def test_new_deck(self):
        my_deck = Deck()
        self.assertEqual(len(my_deck), 52)
        my_deck.shuffle()
        print(my_deck)
        last_card = my_deck[-1]

        hit_card = my_deck.deal()
        self.assertEqual(len(my_deck), 51)
        self.assertEqual(last_card, hit_card)
        print(f"last card was {hit_card}")

if __name__ == '__main__':
    unittest.main()