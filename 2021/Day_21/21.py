import os
import copy
import collections
import pytest
import functools

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''Player 1 starting position: 4
Player 2 starting position: 8
'''

def solve_1(lines):
    p1_pos = int(lines[0].split(": ")[1])
    p2_pos = int(lines[1].split(": ")[1])
    die = 1
    roll = 0
    score_1, score_2 = 0,0
    turn_1 = True
    while score_1 < 1000 and score_2 < 1000:
        value = (die + die+1 + die+2)%10
        if value == 0: value = 10
        if turn_1:
            p1_pos = (p1_pos + value)%10
            if p1_pos == 0: p1_pos = 10
            score_1 += p1_pos
            turn_1 = False
        else:
            p2_pos = (p2_pos + value)%10
            if p2_pos == 0: p2_pos = 10
            turn_1 = True
            score_2 += p2_pos
        die += 3
        if die > 1000: die-= 1000
        roll += 3
    if score_1 > score_2:
        return score_2 * roll
    else:
        return score_1 * roll

def solve_2(lines):
    p1 = int(lines[0].split(": ")[1])
    p2 = int(lines[1].split(": ")[1])
    # Each roll generates 27 possible outcomes
    die_rolls = collections.defaultdict(int)
    for x in range(1,4):
        for y in range(1,4):
            for z in range(1,4):
                die_rolls[x+y+z] += 1

    # This is super handy!
    @functools.lru_cache(maxsize = None)
    def compute_win(p1_pos, p1_score, p2_pos, p2_score):
        p1_wins, p2_wins = 0,0
        for p, val in die_rolls.items():
            new_p1_pos = (p1_pos + p)%10
            if new_p1_pos == 0: new_p1_pos = 10
            new_p1_score = p1_score + new_p1_pos
            if new_p1_score >= 21:
                p1_wins += val
            else:
                p2_wins_recurse, p1_wins_recurse = compute_win(p2_pos, p2_score, new_p1_pos, new_p1_score)
                p1_wins += p1_wins_recurse * val
                p2_wins += p2_wins_recurse * val
        return p1_wins, p2_wins
    
    p1_win, p2_win = compute_win(p1, 0, p2, 0)
    return max(p1_win, p2_win)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))