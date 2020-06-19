from game.rank import Rank
from game.suit import Suit
from game.deck import Deck
from game.player import Player
from utils import BlackjackUtils

playing = True


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

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while playing and hand.value() < 21:
        next_step = input("Hit or stand? ")
        if "hit" == next_step.lower():
            hit(deck, hand)
        else:
            break

def show_some(player):
    if len(player.hand.cards) > 0:
        print(f"{player.name} has {player.hand.cards[0]} and {len(player.hand.cards)-1} more")
    else:
        print(f"{player.name} has no cards")
    
def show_all(player):    
    if len(player.hand.cards)>0:
        print(f"{player.name} has {player.hand.cards}, worth {player.hand.value()}")
    else:
        print(f"{player.name} has no cards")

def prepare(deck, player):
    hit(deck,player.hand)
    hit(deck,player.hand)


while True:
    # Print an opening statement
    print("BLACKJACK light")
    dealer = Player("dealer", BlackjackUtils.calculate_value)
    human_player = Player("player", BlackjackUtils.calculate_value)

    show_some(dealer)
    show_all(human_player)
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    print("Shuffling...")
    deck.shuffle()

    print("Prepare dealer...")
    prepare(deck,dealer)

    print("Prepare player...")
    prepare(deck,human_player)
    
    # Set up the Player's chips
    # Prompt the Player for their bet
    take_bet()

    # Show cards (but keep one dealer card hidden)
    show_some(dealer)
    show_all(human_player)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, human_player.hand)
        
        # Show cards (but keep one dealer card hidden)
        show_all(dealer)
        show_all(human_player)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        

        break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    
    
    # Show all cards
    
    # Run different winning scenarios
        
    
    # Inform Player of their chips total 
    
    # Ask to play again

    break