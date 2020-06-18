class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"
    
    def __repr__(self):
        return str(self)

    def value(self):
        return self.rank.value