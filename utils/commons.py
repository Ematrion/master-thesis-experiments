from rstt import Ranking, BasicElo, BasicGlicko, BasicOS
from rstt.stypes import SPlayer
from rstt.ranking import GameByGame, BatchGame, PlayerChecker, KeyModel, GaussianModel


import trueskill
from openskill.models import PlackettLuce
import numpy as np




# TrueSkill integration in RSTT
class TS(Ranking):
    def __init__(self, name: str, players: list[SPlayer] | None = None):
        env = trueskill.TrueSkill()
        super().__init__(name=name,
                         datamodel=GaussianModel(template=env.create_rating),
                         handler=GameByGame(),
                         backend=env,
                         players=players)


class PlayerTotalWin:
    def __init__(self, default: float = -1.0, scope: int = np.iinfo(np.int32).max):
        self.default = default
        self.scope = scope

    def rate(self, player: SPlayer, *args, **kwargs) -> float:
        return self._win_rate(player)

    def _win_rate(self, player: SPlayer):
        games = player.games()
        if games:
            games = games[-self.scope:]
            total = len(games)
        else:
            total = self.default
        return total
    

class PlayerWins(Ranking):
    def __init__(self, name: str,
                 default: float = -1.0,
                 scope: int = np.iinfo(np.int32).max,
                 players: list[SPlayer] | None = None):

        super().__init__(name,
                         datamodel=KeyModel(default=default),
                         backend=PlayerTotalWin(default=default, scope=scope),
                         handler=PlayerChecker(),
                         players=players)
        # incase player already played games
        self.update()

    def forward(self, *args, **kwargs):
        self.handler.handle_observations(
            datamodel=self.datamodel, infer=self.backend, players=self.players())
        

def rankings(population: list[SPlayer]) -> list[Ranking]:
    elo = BasicElo(name='Elo - GBG', players=population)
    elobg = BasicElo(name='Elo - Batch', players=population)
    elobg.handler = BatchGame()
    glicko = BasicGlicko(name='Gliko - Batch', players=population)
    glickogbg = BasicGlicko(name='Glicko- GBG', players=population)
    glickogbg.handler = GameByGame()
    glickogbg.handler.query = glicko.handler.query
    glickogbg.handler.output_formater = glicko.handler.output_formater
    ts = TS('Trueskill', players=population)
    os = BasicOS('OS - PlackettLuce', model=PlackettLuce(), players=population)
    #return [elo, elobg, glickogbg, glicko, ts, os]
    return [elo, glicko, ts, os]