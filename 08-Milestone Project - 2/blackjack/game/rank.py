
from enum import Enum, auto
class Rank(Enum):
    '''
    Enum class\n
    from Rank import Rank\n
    rank = Rank.ACE\n
    print (rank.value)
    '''

    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str(self)