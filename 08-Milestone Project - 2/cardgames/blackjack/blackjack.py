from game.rank import Rank
from game.suit import Suit
from game.deck import Deck
from game.player import Player
from blackjack.utils import BlackjackUtils

class Blackjack():

    def __init__(self):
        self.playing = True

    def take_bet(self, player):

        is_bet_placed = False
        while not is_bet_placed: 
            try:
                bet = input("Place your bet: ")
                player.chips.place_bet(int(bet))
                is_bet_placed = True
            except IndexError as e:
                print(e.args[0])
            except:
                print("That's not a valid bet.")

    def hit(self, deck,hand):
        hand.add_card(deck.deal())

    def hit_or_stand(self, deck,hand):

        next_step = input("Hit or stand? ")
        if "hit" == next_step.lower():
            self.hit(deck, hand)
        else:
            self.playing = False

    def show_some(self, player):
        if len(player.hand.cards) > 0:
            print(f"{player.name} has {player.hand.cards[0]} and {len(player.hand.cards)-1} more")
        else:
            print(f"{player.name} has no cards")
        
    def show_all(self, player):    
        if len(player.hand.cards)>0:
            print(f"{player.name} has {player.hand.cards}, worth {player.hand.value()}")
        else:
            print(f"{player.name} has no cards")

    def prepare(self, deck, player):
        self.hit(deck,player.hand)
        self.hit(deck,player.hand)

    def is_blackjack(self, hand):
        return len(hand.cards) == 2 and hand.value() == 21

    def handle_win(self, player):
        player.chips.win_bet()

    def handle_loss(self, player):
        player.chips.lose_bet()

    def evaluate(self, player, dealer):
        '''
        If the player is dealt an Ace and a ten-value card (called a "blackjack" or "natural"), and the dealer does not, the player wins and usually receives a bonus.
        If the player exceeds a sum of 21 ("busts"); the player loses, even if the dealer also exceeds 21.
        If the dealer exceeds 21 ("busts") and the player does not; the player wins.
        If the player attains a final sum higher than the dealer and does not bust; the player wins.
        If both dealer and player receive a blackjack or any other hands with the same sum, called a "push", no one wins.
        '''
        if self.is_blackjack(player.hand) and not self.is_blackjack(dealer.hand):
            self.handle_win(player)
            return player
        elif player.hand.value() > 21:
            self.handle_loss(player)
            return dealer
        elif dealer.hand.value() > 21:
            self.handle_win(player)
            return player
        elif player.hand.value() > dealer.hand.value():
            self.handle_win(player)
            return player
        elif player.hand.value() == dealer.hand.value():
            return None

    def play(self):
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

            self.show_some(dealer)
            self.show_all(human_player)
            
            # Create & shuffle the deck, deal two cards to each player
            deck = Deck()
            print("Shuffling...")
            deck.shuffle()

            print("Prepare dealer...")
            self.prepare(deck,dealer)

            print("Prepare player...")
            self.prepare(deck,human_player)
            
            # Set up the Player's chips
            # Prompt the Player for their bet
            self.take_bet(human_player)

            # Show cards (but keep one dealer card hidden)
            self.show_some(dealer)
            self.show_all(human_player)

            is_player_busted = False
            while self.playing:  # recall this variable from our hit_or_stand function
                
                # Prompt for Player to Hit or Stand
                self.hit_or_stand(deck, human_player.hand)
                
                # Show cards (but keep one dealer card hidden)
                self.show_some(dealer)
                self.show_all(human_player)
                
                # If player's hand exceeds 21, run player_busts() and break out of loop
                if human_player.hand.value() > 21:
                    is_player_busted = True
                    self.playing = False

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if not is_player_busted:
                while dealer.hand.value() < 17:
                    self.hit(deck, dealer.hand)
            
            # Show all cards
            self.show_all(dealer)
            self.show_all(human_player)
            
            # Run different winning scenarios
            winner = self.evaluate(human_player, dealer)
            if (human_player == winner):
                print(f"\n\t{human_player.name} wins and has {len(human_player.chips)} in posession\n")
            elif (dealer == winner):
                print(f"\n\t{human_player.name} looses and has {len(human_player.chips)} in posession\n")
            else:
                print("Push. No change in chips.")
            
            # Inform Player of their chips total 
            
            # Ask to play again
            if input("Do you want to play again? [y/N] ").lower().startswith('y'):
                self.playing = True
                continue
            else: 
                break