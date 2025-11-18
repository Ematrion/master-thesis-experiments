from typing import Protocol
from scipy import stats
from rstt import Ranking, Competition
from rstt.ranking import Elo, Glicko

import trueskill
from openskill.models import PlackettLuce

class evaluation(Protocol):
    def __call__(self, ranking: Ranking, event: Competition, ref: Ranking) -> float:
        ...
        
class rmetric(Protocol):
    def __call__(self, ranking: Ranking, event: Competition) -> float:
        ...

def ktcorr(ranking: Ranking, gt: Ranking, *args, **kwargs) -> float:
    return stats.kendalltau([gt.point(p) for p in gt], [ranking.point(p) for p in gt]).statistic # type: ignore 

def game_quality(ranking: Ranking, event: Competition, *args, **kwargs) -> list[float]:
    qualities = []
    for duel in event.games():
        rating1 = ranking.datamodel.get(duel.player1()) # type: ignore
        rating2 = ranking.datamodel.get(duel.player2()) # type: ignore

        if isinstance(ranking.backend, Elo | Glicko):
            expected_score1 = ranking.backend.expectedScore(rating1, rating2)
            expected_score2 = ranking.backend.expectedScore(rating2, rating1)
            expected_score = (expected_score1 + expected_score2) / 2
            quality = 2 * (0.5 - abs(0.5 - expected_score))

        elif isinstance(ranking.backend, trueskill.TrueSkill):
            quality = trueskill.quality_1vs1(rating1, rating2, ranking.backend)

        elif isinstance(ranking.backend, PlackettLuce):
            quality = ranking.backend.predict_draw([[rating1], [rating2]])
        
        qualities.append(quality)
    return qualities


def argmin(elems: list[float]) -> int:
    '''
    Return the index of the minimum element in elems.
    '''
    min_idx = 0
    min_val = elems[0]
    for i in range(1, len(elems)):
        if elems[i] < min_val:
            min_val = elems[i]
            min_idx = i
    return min_idx

def argmax(elems: list[float]) -> int:
    '''
    Return the index of the maximum element in elems.
    '''
    max_idx = 0
    max_val = elems[0]
    for i in range(1, len(elems)):
        if elems[i] > max_val:
            max_val = elems[i]
            max_idx = i
    return max_idx
