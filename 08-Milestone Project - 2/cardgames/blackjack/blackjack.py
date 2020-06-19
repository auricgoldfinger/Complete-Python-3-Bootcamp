from game.rank import Rank
from game.suit import Suit
from blackjack.utils import BlackjackUtils

rank_values = {}
for rank in Rank:
    rank_values[rank] = BlackjackUtils.rankEvaluator(rank)

print(rank_values)