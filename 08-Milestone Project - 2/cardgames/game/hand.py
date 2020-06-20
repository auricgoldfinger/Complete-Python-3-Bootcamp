from game.card import Card
from game.rank import Rank

class Hand:
    def __init__(self, value_calculator):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value_calculator = value_calculator

    def add_card(self,card):
        self.cards.append(card)

    def value(self):
        return self.value_calculator(self.cards)
    
    def clear(self):
        self.cards.clear()