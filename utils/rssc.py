from typing import Callable, Any
from scipy import stats

from rstt.stypes import Solver
from rstt import Ranking, Competition

from utils.metrics import rmetric

# protocol
def rssc(name: str, seed: Ranking, cup: type[Competition], solver: Solver, depth: int,
         metric: Callable[..., float], update: bool = True) -> list[Any]:
    results = []
    for i in range(depth):
        tournament = cup(f'{name} - rscc edition {i}', seed, solver)
        tournament.registration(seed.players())
        tournament.run()
        
        if update:
            seed.update(event=tournament)

        results.append(metric(ranking=seed, event=tournament))

    return results