from game.chips import Chips
import unittest

class Test_Chips(unittest.TestCase):

    def test_simple_chips(self):
        my_chips = Chips()
        self.assertRaises(IndexError, my_chips.place_bet,200)

        my_chips.place_bet(50)
        my_chips.win_bet()
        self.assertEqual(my_chips.total, 150)

        my_chips.place_bet(60)
        my_chips.lose_bet()
        self.assertEqual(my_chips.total, 90)

if __name__ == "__main__":
    unittest.main()