import pytest

from utils import treeprob as tp



@pytest.fixture
def seed8():
    return list(range(8))

@pytest.fixture
def prob8():
    return [[0.5, 0.57, 0.64, 0.71, 0.79, 0.86, 0.93, 1.0],
            [0.43, 0.5, 0.57, 0.64, 0.71, 0.79, 0.86, 0.93],
            [0.36, 0.43, 0.5, 0.57, 0.64, 0.71, 0.79, 0.86],
            [0.29, 0.36, 0.43, 0.5, 0.57, 0.64, 0.71, 0.79],
            [0.21, 0.29, 0.36, 0.43, 0.5, 0.57, 0.64, 0.71],
            [0.14, 0.21, 0.29, 0.36, 0.43, 0.5, 0.57, 0.64],
            [0.07, 0.14, 0.21, 0.29, 0.36, 0.43, 0.5, 0.57],
            [0.0, 0.07, 0.14, 0.21, 0.29, 0.36, 0.43, 0.5]]

@pytest.fixture
def bracket8(seed8, prob8):
    return tp.treeprob(seed8, prob8)


def test_init_treeprob(seed8):
    pre_round = tp.init_treeprob(seed8)
    
    # every one plays
    assert len(pre_round) == len(seed8)
    # every 'potential player' consist of exactly one player
    assert all(len(pr) == 1 for pr in pre_round)
    # that player is guarantee to play the first round 
    assert all(list(pr.values())[0] == 1.0 for pr in pre_round)
    
def test_make_first_round(seed8):
    pre_round = tp.init_treeprob(seed8)
    matches = tp.make_round(pre_round)
    # a game for every two players
    assert len(matches) == len(seed8)//2
    for match in matches:
        # a match is a confrontation between two 'potential players'
        assert len(match) == 2
        
def test_solve_first_round(seed8, prob8):
    pre_round = tp.init_treeprob(seed8)
    matches = tp.make_round(pre_round)
    post_round = tp.round_results(matches, prob8)
    
    # every game ends up in a result
    assert len(post_round) == len(matches)
    
    # each player has a chance to win the game
    for post, game in zip(post_round, matches):
        assert len(post) == len(game[0]) + len(game[1])
    
    # there is always a winner in each game
    assert all(sum(post.values()) == 1.0 for post in post_round)

def test_always_a_winner(bracket8: list[tp.RoundResult]):
    for round in bracket8:
        for candidate in round:
            assert pytest.approx(sum(candidate.values())) == 1.0

def test_only_one_winner(bracket8: list[tp.RoundResult]):
    final_round = bracket8[-1]
    # only one potential winner in the final round
    assert len(final_round) == 1
    # each initial candidate has a probability to win
    assert set(final_round[0].keys()) == {c for candidate in bracket8[0] for c in candidate.keys()}
    
def test_score_prob(bracket8: tp.TreeProb, seed8):
    for seed in seed8:
        total_prob = 0.0
        for score in range(len(bracket8)):
            total_prob += tp.score_prob(seed, score, bracket8)
        assert pytest.approx(total_prob) == 1.0
        
def test_sum_of_expected_scores(bracket8: tp.TreeProb, seed8):
    # the number of match played
    total_score = sum([len(r) for r in bracket8[1:]])
    total_exp_score = 0.0
    for seed in seed8:
        total_exp_score += tp.expected_score(seed, bracket8)
    # sum of expected scores equals number of rounds
    assert pytest.approx(total_exp_score) == total_score
    
