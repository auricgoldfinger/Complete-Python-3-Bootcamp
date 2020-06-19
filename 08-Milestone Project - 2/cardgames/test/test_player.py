import unittest
from game.player import Player
from blackjack.utils import BlackjackUtils

class Test_Player(unittest.TestCase):

    def test_simple_player(self):
        my_player = Player("Myself", BlackjackUtils.calculate_value)
        self.assertEqual("Myself", my_player.name)

if __name__ == "__main__":
    unittest.main()