import unittest
from game.player import Player
from blackjack.utils import BlackjackUtils

class Test_Player(unittest.TestCase):

    def test_simple_player(self):
        my_player = Player(BlackjackUtils.calculate_value)

if __name__ == "__main__":
    unittest.main()