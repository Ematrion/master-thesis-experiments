from typing import Protocol
from scipy import stats
from rstt import Ranking, Competition


class evaluation(Protocol):
    def __call__(self, ranking: Ranking, event: Competition, ref: Ranking) -> float:
        ...
        
class rmetric(Protocol):
    def __call__(self, ranking: Ranking, event: Competition) -> float:
        ...

def ktcorr(ranking: Ranking, gt: Ranking, *args, **kwargs) -> float:
    return stats.kendalltau([gt.point(p) for p in gt], [ranking.point(p) for p in gt]).statistic # type: ignore 


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