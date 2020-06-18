from game.card import Card
from game.rank import Rank
from game.suit import Suit

class Deck:

    def __init__(self):
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))
    
    def __str__(self):
        return str(self.cards)
        
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self.cards)