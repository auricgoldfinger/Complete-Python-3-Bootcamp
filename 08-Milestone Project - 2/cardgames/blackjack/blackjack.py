from game.rank import Rank
from game.suit import Suit
from game.deck import Deck
from game.player import Player
from utils import BlackjackUtils

dealer = Player("dealer", BlackjackUtils.calculate_value)
human_player = Player("player", BlackjackUtils.calculate_value)
deck = Deck()

def take_bet():

    is_bet_placed = False
    while not is_bet_placed: 
        try:
            bet = input("Place your bet: ")
            human_player.chips.place_bet(int(bet))
            is_bet_placed = True
        except IndexError as e:
            print(e.args[0])
        except:
            print("That's not a valid bet.")

def hit(deck,hand):
    hand.add_card(deck.deal())
    if hand.value() > 21:
        print("Busted")
    elif hand.value() == 21:
        print("Won!")
    else:
        print("Continue")

take_bet()
deck.shuffle()
hit(deck, human_player.hand)