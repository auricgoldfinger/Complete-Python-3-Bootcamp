from game.rank import Rank
from game.suit import Suit
from game_utils import Game_Utils

rank_values = {}
for rank in Rank:
    rank_values[rank] = Game_Utils.rankEvaluator(rank)

print(rank_values)