import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

'''
A -> Rock
B -> Paper
C -> Scissor

X -> Rock
Y -> Paper
Z -> Scissor
'''
test_input = \
'''A Y
B X
C Z
'''

score = [[4,1,7],[8,5,2],[3,9,6]]

def get_score(opponent, me):
    col, row = ord(opponent) - ord('A'), ord(me) - ord('X')
    return score[row][col]

def solve_1(lines):
    total_score = 0
    for line in lines:
        opponent,me = line.split(" ")
        total_score += get_score(opponent,me)
    return total_score

def get_choice_for_outcome(opponent, outcome):
    if outcome == 'X': 
        # X = lose
        if opponent == 'A': 
            # A = Rock
            # Play Scissor
            return 'Z' 
        if opponent == 'B': 
            # B = Paper
            # Play Rock
            return 'X' 
        else:
            return 'Y'
    elif outcome == 'Y': 
        # Y = draw
        if opponent == 'A':
            return 'X'
        elif opponent == 'B':
            return 'Y'
        else:
            return 'Z'
    else: # Z = win
        if opponent == 'A': 
            # Rock
            # Play Paper
            return 'Y'
        elif opponent == 'B': 
            # Paper
            # Play Scissor
            return 'Z'
        else:
            return 'X'

def solve_2(lines):
    total_score = 0
    for line in lines:
        opponent, outcome = line.split(" ")
        me = get_choice_for_outcome(opponent, outcome)
        total_score += get_score(opponent, me)
    return total_score

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))