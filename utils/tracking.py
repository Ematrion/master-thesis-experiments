from typing import Any
from dataclasses import dataclass
from collections import Counter

from rstt import Ranking, Duel
from rstt.stypes import SPlayer, SMatch, Event


Encounters = Counter[tuple[int, int]]

@dataclass
class RSSC_RESULT:
    ratings: dict[SPlayer, Any]
    skills: dict[SPlayer, float]
    games: list[SMatch]
    
def rssc_data(ranking: Ranking, event: Event, ref: Ranking) -> RSSC_RESULT:
    return RSSC_RESULT(
        ratings={p: ranking.datamodel.get(p) for p in ranking},
        skills={p: p.level() for p in ref},
        games=event.games() # type: ignore
    )
    
def load_data(results: list[RSSC_RESULT]) -> list[SMatch]:
    return [game for result in results for game in result.games]

def load_ratings(ranking: Ranking, result: RSSC_RESULT) -> Ranking:
    for p, r in result.ratings.items():
        ranking.set_rating(p, r)
    return ranking

def train_ranking(ranking: Ranking, results: list[RSSC_RESULT]) -> Ranking:
    for result in results:
        ranking.update(games=result.games)
    return ranking

def seen_data(games: list[Duel], ref: Ranking) -> Encounters:
    return Counter([(ref[duel.player1()], ref[duel.player2()]) for duel in games]) # type: ignore

def unseen_data(domain: Encounters, ref: Ranking) -> Encounters:
    nb = len(ref)
    return Counter([(i, j) for i in range(nb) for j in range(nb) if (i, j) not in domain and i != j])

def domain(mm_domain: Encounters, ref: Ranking) -> list[list[int]]:
    nb = len(ref)
    return [[mm_domain[(i, j)] for i in range(nb)] for j in range(nb)]
