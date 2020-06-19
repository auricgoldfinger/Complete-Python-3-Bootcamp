from game.rank import Rank
from game.suit import Suit
from game.deck import Deck
from game.player import Player
from utils import BlackjackUtils

playing = True

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
    value = hand.value()
    print(f"Holding {hand.cards}  ({value})")
    if value > 21:
        print("Busted")
    elif value == 21:
        print("Won!")
    else:
        print("Continue")

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while playing and hand.value() < 21:
        next_step = input("Hit or stand? ")
        if "hit" == next_step.lower():
            hit(deck, hand)
        else:
            break

take_bet()
deck.shuffle()
hit_or_stand(deck, human_player.hand)