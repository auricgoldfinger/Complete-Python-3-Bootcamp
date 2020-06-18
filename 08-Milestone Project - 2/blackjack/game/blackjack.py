from game.rank import Rank
from game.suit import Suit

rank_values = {}
for rank in Rank:
    rank_value = rank.value
    if Rank.ACE == rank:
        rank_value = 11
    elif Rank.JACK == rank or Rank.QUEEN == rank or Rank.KING == rank:
        rank_value = 10
    
    rank_values[rank] = rank_value

print(rank_values)