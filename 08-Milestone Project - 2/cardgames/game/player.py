from game.hand import Hand
from game.chips import Chips

class Player():

    def __init__(self, value_calculator):
        self.hand = Hand(value_calculator)
        self.chips = Chips()