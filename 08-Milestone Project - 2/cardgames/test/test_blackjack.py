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

    def test_hit(self):
        deck = Deck()
        hand = Hand(BlackjackUtils.calculate_value)
        blackjack = Blackjack()
        blackjack.hit(deck, hand)
        self.assertEqual(1, len(hand.cards))
        self.assertEqual(10, hand.value()) # deck wasn't shuffled
        self.assertEqual(Suit.CLUBS, hand.cards[0].suit)
        self.assertEqual(Rank.KING, hand.cards[0].rank)

    def test_prepare(self):
        player = Player("player", BlackjackUtils.calculate_value)
        blackjack = Blackjack()
        deck = Deck()

        blackjack.prepare(deck, player)
        self.assertEqual(2, len(player.hand.cards))
        self.assertEqual(Suit.CLUBS, player.hand.cards[0].suit)
        self.assertEqual(Rank.KING, player.hand.cards[0].rank)
        self.assertEqual(Suit.CLUBS, player.hand.cards[1].suit)
        self.assertEqual(Rank.QUEEN, player.hand.cards[1].rank)

    def test_is_blackjack(self):
        blackjack = Blackjack()
        hand = Hand(BlackjackUtils.calculate_value)
        hand.add_card(Card(Suit.CLUBS, Rank.ACE))
        hand.add_card(Card(Suit.HEARTS, Rank.QUEEN))
        self.assertTrue(blackjack.is_blackjack(hand))
        hand.add_card(Card(Suit.SPADES, Rank.ACE))
        self.assertFalse(blackjack.is_blackjack(hand))

        hand.clear()
        hand.add_card(Card(Suit.CLUBS, Rank.ACE))
        hand.add_card(Card(Suit.DIAMONDS, Rank.SIX))
        hand.add_card(Card(Suit.DIAMONDS, Rank.FOUR))
        self.assertFalse(blackjack.is_blackjack(hand))

        hand.clear()
        hand.add_card(Card(Suit.CLUBS, Rank.ACE))
        hand.add_card(Card(Suit.DIAMONDS, Rank.FIVE))
        self.assertFalse(blackjack.is_blackjack(hand))

    def prepare_winning_scenarios(self):
        player = Player("player", BlackjackUtils.calculate_value)
        dealer = Player("dealer", BlackjackUtils.calculate_value)
        
        blackjack = Blackjack()
        
        player.chips.place_bet(20)

        return (player, dealer, blackjack)

    def test_player_has_won_with_blackjack(self):
        player, dealer, blackjack = self.prepare_winning_scenarios()

        # player has blackjack
        player.chips.place_bet(20)
        player.hand.add_card(Card(Suit.HEARTS, Rank.ACE))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        self.assertTrue(blackjack.is_blackjack(player.hand))

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.NINE))
        dealer.hand.add_card(Card(Suit.HEARTS, Rank.KING))

        self.assertEqual(player, blackjack.evaluate(player, dealer))
        self.assertEqual(120, len(player.chips))

    def test_player_has_won_with_dealer_bust(self):
        player, dealer, blackjack = self.prepare_winning_scenarios()

        player.hand.add_card(Card(Suit.HEARTS, Rank.FIVE))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        player.hand.add_card(Card(Suit.SPADES, Rank.FOUR))

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.FIVE))
        dealer.hand.add_card(Card(Suit.CLUBS, Rank.EIGHT))
        dealer.hand.add_card(Card(Suit.HEARTS, Rank.KING))

        self.assertEqual(player, blackjack.evaluate(player, dealer))
        self.assertEqual(120, len(player.chips))

    def test_player_has_won_with_heigher_value_not_blackjack(self):
        player, dealer, blackjack = self.prepare_winning_scenarios()
        
        player.hand.add_card(Card(Suit.HEARTS, Rank.FIVE))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        player.hand.add_card(Card(Suit.SPADES, Rank.FOUR))
        self.assertEqual(19, player.hand.value())

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.SIX))
        dealer.hand.add_card(Card(Suit.CLUBS, Rank.EIGHT))
        dealer.hand.add_card(Card(Suit.HEARTS, Rank.FOUR))
        self.assertEqual(18, dealer.hand.value())

        self.assertEqual(player, blackjack.evaluate(player, dealer))
        self.assertEqual(120, len(player.chips))

    ##
    ## PLAYER LOST
    ##

    def test_player_has_lost_with_bust_dealer_blackjack(self):
        player, dealer, blackjack = self.prepare_winning_scenarios()
        
        player.hand.add_card(Card(Suit.HEARTS, Rank.SIX))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        player.hand.add_card(Card(Suit.SPADES, Rank.TEN))
        self.assertEqual(26, player.hand.value())

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.ACE))
        dealer.hand.add_card(Card(Suit.CLUBS, Rank.KING))
        self.assertEqual(21, dealer.hand.value())
        self.assertTrue(blackjack.is_blackjack(dealer.hand))

        self.assertEqual(dealer, blackjack.evaluate(player, dealer))
        self.assertEqual(80, len(player.chips))

    def test_player_has_lost_with_bust_dealer_twentyone(self):
        player, dealer, blackjack = self.prepare_winning_scenarios()
        
        player.hand.add_card(Card(Suit.HEARTS, Rank.SIX))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        player.hand.add_card(Card(Suit.SPADES, Rank.TEN))
        self.assertEqual(26, player.hand.value())

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.SIX))
        dealer.hand.add_card(Card(Suit.CLUBS, Rank.KING))
        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.FIVE))
        self.assertEqual(21, dealer.hand.value())
        self.assertFalse(blackjack.is_blackjack(dealer.hand))

        self.assertEqual(dealer, blackjack.evaluate(player, dealer))
        self.assertEqual(80, len(player.chips))

    def test_player_has_lost_with_lower_value_not_blackjack(self):
        player, dealer, blackjack = self.prepare_winning_scenarios()
        
        player.hand.add_card(Card(Suit.HEARTS, Rank.SIX))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        player.hand.add_card(Card(Suit.SPADES, Rank.THREE))
        self.assertEqual(19, player.hand.value())

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.FIVE))
        dealer.hand.add_card(Card(Suit.CLUBS, Rank.EIGHT))
        dealer.hand.add_card(Card(Suit.HEARTS, Rank.SEVEN))
        self.assertEqual(20, dealer.hand.value())

        self.assertEqual(dealer, blackjack.evaluate(player, dealer))
        self.assertEqual(80, len(player.chips))

    def test_player_has_lost_with_lower_value_dealer_has_twentyone(self):
        player, dealer, blackjack = self.prepare_winning_scenarios()
        
        player.hand.add_card(Card(Suit.HEARTS, Rank.SIX))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        player.hand.add_card(Card(Suit.SPADES, Rank.THREE))
        self.assertEqual(19, player.hand.value())

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.THREE))
        dealer.hand.add_card(Card(Suit.CLUBS, Rank.EIGHT))
        dealer.hand.add_card(Card(Suit.HEARTS, Rank.TEN))
        self.assertEqual(21, dealer.hand.value())

        self.assertEqual(dealer, blackjack.evaluate(player, dealer))
        self.assertEqual(80, len(player.chips))

    def test_player_has_lost_with_lower_value_dealer_has_blackjack(self):
        player, dealer, blackjack = self.prepare_winning_scenarios()
        
        player.hand.add_card(Card(Suit.HEARTS, Rank.SIX))
        player.hand.add_card(Card(Suit.CLUBS, Rank.QUEEN))
        player.hand.add_card(Card(Suit.SPADES, Rank.THREE))
        self.assertEqual(19, player.hand.value())

        dealer.hand.add_card(Card(Suit.DIAMONDS, Rank.ACE))
        dealer.hand.add_card(Card(Suit.CLUBS, Rank.KING))
        self.assertEqual(21, dealer.hand.value())
        self.assertTrue(blackjack.is_blackjack(dealer.hand))

        self.assertEqual(dealer, blackjack.evaluate(player, dealer))
        self.assertEqual(80, len(player.chips))


if __name__ == '__main__':
    unittest.main()