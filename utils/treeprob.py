

PlayProb = dict[int, float]
ProbMatch = tuple[PlayProb, PlayProb]
RoundMatch = list[ProbMatch]
RoundResult = list[PlayProb]
TreeProb = list[RoundResult]


# --- computations functions --- #
def make_round(seeds: RoundResult) -> RoundMatch:
    '''
    Move into the next round of the bracket by pairing the players.
    '''
    matches: RoundMatch = []
    for i in range(0, len(seeds), 2):
        game = (seeds[i], seeds[i+1])
        matches.append(game)
    return matches

def solve_match(ProbMatch, prob: list[list[float]]) -> PlayProb:
    '''
    Given potential opponents and their probabilities to reach the match,
    output the probabilities of each player to win the match.
    '''
    winProb: PlayProb = {} # probability to play the next round
    for p1, prob1 in ProbMatch[0].items():
        p1_prob = 0.0
        for p2, prob2 in ProbMatch[1].items():
            p1_prob += prob[p1][p2] * prob1 * prob2
        winProb[p1] = p1_prob
    for p2, prob2 in ProbMatch[1].items():
        p2_prob = 0.0
        for p1, prob1 in ProbMatch[0].items():
            p2_prob += prob[p2][p1] * prob1 * prob2
        winProb[p2] = p2_prob
    return winProb

def round_results(matches: RoundMatch, prob: list[list[float]]) -> RoundResult:
    '''
    Compute the result probabilities of a round given the match probabilities.
    '''
    return [solve_match(match, prob) for match in matches]

def init_treeprob(seeds: list[int]) -> RoundResult:
    '''
    Every seeds play the first round with probability 1.

    i.e no by round, seeds must be length of power of 2.
    '''
    return [{seed: 1.0} for seed in seeds]

def treeprob(seeds: list[int], prob: list[list[float]]) -> list[RoundResult]:
    '''
    Given the initial seeds and the pairwise win probabilities,
    compute the probability distribution of each round in the bracket.
    '''
    rounds: list[RoundResult] = []
    current_round = init_treeprob(seeds)
    rounds.append(current_round)

    while len(current_round) > 1:
        matches = make_round(current_round)
        current_round = round_results(matches, prob)
        rounds.append(current_round)

    return rounds


# --- analysis functions --- #
def round_prob(result: TreeProb, round: int) -> PlayProb:
    '''
    flatten PlayProb of a round into a single dictionary.
    '''
    return {k: v for playprobs in result[round] for k, v in playprobs.items()}

def play_prob(seed: int, r: int, tree: TreeProb) -> float:
    '''
    return the probability that a seed plays in a given round of the bracket
    '''
    # ??? how much error does this introduce
    return sum([candidate.get(seed, 0.0) for candidate in tree[r]])

def score_prob(seed: int, score: int, tree: TreeProb) -> float:
    '''
    return the probability that a seed achieves a given score in the bracket
    (i.e wins 'score' number of rounds)
    '''
    return play_prob(seed, score, tree) - play_prob(seed, score + 1, tree) if score != len(tree) - 1 else play_prob(seed, score, tree)

def expected_score(seed: int, tree: TreeProb) -> float:
    '''
    return the expected score of a seed in the bracket
    '''
    exp_score = 0.0
    for score in range(len(tree)):
        exp_score += score * score_prob(seed, score, tree)
    return exp_score


if __name__ == '__main__':
    # example usage
    seeds = [0, 7, 3, 4, 1, 6, 2, 5]
    prob = [[0.5, 0.57, 0.64, 0.71, 0.79, 0.86, 0.93, 1.0],
            [0.43, 0.5, 0.57, 0.64, 0.71, 0.79, 0.86, 0.93],
            [0.36, 0.43, 0.5, 0.57, 0.64, 0.71, 0.79, 0.86],
            [0.29, 0.36, 0.43, 0.5, 0.57, 0.64, 0.71, 0.79],
            [0.21, 0.29, 0.36, 0.43, 0.5, 0.57, 0.64, 0.71],
            [0.14, 0.21, 0.29, 0.36, 0.43, 0.5, 0.57, 0.64],
            [0.07, 0.14, 0.21, 0.29, 0.36, 0.43, 0.5, 0.57],
            [0.0, 0.07, 0.14, 0.21, 0.29, 0.36, 0.43, 0.5]]

    rounds = treeprob(seeds, prob)
    
    for r in range(len(rounds)):
        rp = round_prob(rounds, r)
        print(f'Round {r} prob: {rp}')
        
    for seed in seeds:
        print()
        print(seed)
        for score in range(len(rounds)):
            pb = play_prob(seed, score, rounds)
            print(f'Score {score} play_prob: {pb}', 'score prob:', score_prob(seed, score, rounds))

        exp_score = expected_score(seed, rounds)
        print(f'Seed {seed} expected_score: {exp_score}')
    
    
    print()
    print(rounds)

# prob (score) = prob(round) / prob(round + 1)