from game.hand import Hand
from game.chips import Chips

class Player():

    def __init__(self, name, value_calculator):
        self.name = name
        self.hand = Hand(value_calculator)
        self.chips = Chips()