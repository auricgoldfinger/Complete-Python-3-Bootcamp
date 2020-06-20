from blackjack.blackjack import Blackjack
from blackjack.utils import BlackjackUtils
from game.player import Player
from game.card import Card
from game.chips import Chips
from game.deck import Deck
from game.hand import Hand
from game.rank import Rank
from game.suit import Suit
import unittest

class Test_Blackjack(unittest.TestCase):

    def test_player_has_blackjack(self):
        player = Player("player", BlackjackUtils.calculate_value)
        dealer = Player("dealer", BlackjackUtils.calculate_value)
        blackjack = Blackjack()
        # player has blackjack
        player.chips.place_bet(20)
        player.hand.add_card(Card(Suit.HEARTS, Rank.ACE))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.NINE))
        dealer.hand.add_card(Card(Suit.HEARTS, Rank.KING))

        self.assertEqual(player, blackjack.evaluate(player, dealer))
        self.assertEqual(120, len(player.chips))

if __name__ == '__main__':
    unittest.main()