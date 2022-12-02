from typing import Optional, Tuple

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

left_points = {
    'A': ROCK, 
    'B': PAPER,
    'C': SCISSORS
}

right_points = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS, 
}

shape_score = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

outcome_score = {
    'won': 6,
    'draw': 3,
    'lost': 0,
}

win_tables = [
    (ROCK, PAPER),
    (PAPER, SCISSORS),
    (SCISSORS, ROCK),
]

def get_points(l: str, r: str) -> Optional[Tuple[int, int]]:
    lsp = shape_score[l]
    rsc = shape_score[r]

    if l == r:
        result = lsp + outcome_score['draw']
        return result, result

    if outcome := next((win_table for win_table in win_tables if win_table == (l, r)), None):
        return outcome_score['lost'] + lsp, outcome_score['won'] + rsc

def part1(left: str, right: str) -> (int, int):
    return get_points(left, right) or swap(get_points(right, left))

rules = {
    SCISSORS: win_tables,
    ROCK: [(r, l) for (l,r) in win_tables],
}

def part2(left: str, right: str) -> (int, int):
    outcome = rules.get(right)
    if outcome:
        (l, r) = next(((l, r) for l, r in outcome if l == left))
    else:
        (l, r) = (left, left)
    return part1(l, r)

def swap(t: tuple) -> tuple:
    t1, t2 = t
    return t2, t1

with open('./input.txt') as f:
    xss = []
    while line := f.readline():
        l, r = line.strip().split(' ')
        xss.append((left_points[l], right_points[r]))

    def get_my_score(part):
        evaluated = [part(*xs) for xs in xss]
        return sum(score for _, score in evaluated)

    print('1', get_my_score(part1))
    print('2', get_my_score(part2))