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
    
    next_step = input("Hit or stand? ")
    if "hit" == next_step.lower():
        hit(deck, hand)
    else:
        playing = False


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

def is_blackjack(hand):
    return len(hand.cards) == 2 and hand.value() == 21

def handle_win(player):
    player.chips.win_bet()
    print(f"{player.name} wins and has {len(player.chips)} in posession")

def handle_loss(player):
    player.chips.lose_bet()
    print(f"{player.name} looses and has {len(player.chips)} in posession")

def evaluate(player, dealer):
    '''
    If the player is dealt an Ace and a ten-value card (called a "blackjack" or "natural"), and the dealer does not, the player wins and usually receives a bonus.
    If the player exceeds a sum of 21 ("busts"); the player loses, even if the dealer also exceeds 21.
    If the dealer exceeds 21 ("busts") and the player does not; the player wins.
    If the player attains a final sum higher than the dealer and does not bust; the player wins.
    If both dealer and player receive a blackjack or any other hands with the same sum, called a "push", no one wins.
    '''
    if is_blackjack(player.hand) and not is_blackjack(dealer.hand):
        handle_win(player)
    elif player.hand.value() > 21:
        handle_loss(player)
    elif dealer.hand.value() > 21:
        handle_win(player)
    elif player.hand.value() > dealer.hand.value():
        handle_win(player)
    elif player.hand.value() == dealer.hand.value():
        print(f"It's a push. No change of chips.")

while True:
    # Print an opening statement

    print("██████╗ ██╗♥     █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗")
    print("██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝")
    print("██████╔╝██║     ███████║██║ ♣   █████╔╝      ██║███████║██║  ♦  █████╔╝ ")
    print("██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██ ♠ ██║██╔══██║██║     ██╔═██╗ ")
    print("██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗")
    print("╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
    print("")

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

    is_player_busted = False
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, human_player.hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(dealer)
        show_all(human_player)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if human_player.hand.value() > 21:
            is_player_busted = True
            playing = False

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if not is_player_busted:
        while dealer.hand.value() < 17:
            hit(deck, dealer.hand)
    
    # Show all cards
    show_all(dealer)
    show_all(human_player)
    
    # Run different winning scenarios
    evaluate(human_player, dealer)
    
    # Inform Player of their chips total 
    
    # Ask to play again
    if input("Do you want to play again? [y/N] ").lower().startswith('y'):
        continue
    else: 
        break