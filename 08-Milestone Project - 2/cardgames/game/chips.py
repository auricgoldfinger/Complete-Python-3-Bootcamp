class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def __len__(self):
        return self.total

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

    def place_bet(self, bet):
        if bet > self.total:
            raise IndexError(f"You can't place a bet of {bet} when you've only have {self.total} left")
        self.bet = int(bet)