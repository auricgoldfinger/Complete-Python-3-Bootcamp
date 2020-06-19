from game.rank import Rank

class BlackjackUtils:

    @staticmethod
    def rankEvaluator(rank):
        rank_value = rank.value
        if Rank.ACE == rank:
            rank_value = 11
        elif Rank.JACK == rank or Rank.QUEEN == rank or Rank.KING == rank:
            rank_value = 10

        return rank_value

    @staticmethod
    def calculate_value(cards):
        result = 0
        if len(cards) > 0:
            nrAces = len(list(filter(lambda c:c.rank == Rank.ACE, cards)))
            # first count the number of other cards
            result = sum(BlackjackUtils.rankEvaluator(card.rank) for card in list(filter(lambda c:c.rank != Rank.ACE, cards)))
            # If there are multiple aces, only one might have the value of 11. Others always have value 1
            result += max(0, nrAces-1)
            nrAces -= max(0, nrAces-1)

            if (nrAces > 0):
                # then handle the remaining ace.
                if (result > 10):
                    # if the sum of all cards + all but one ace is greater than 10, all aces must have value one or we'll go over 21
                    result += nrAces
                else:
                   result += BlackjackUtils.rankEvaluator(Rank.ACE)

        return result