import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''

def solve(lines, count_distinct):
    for i in range(count_distinct-1, len(lines[0])):
        char_set = set()
        for j in range(i, i-count_distinct, -1):
            char_set.add(lines[0][j])
        if len(char_set) == count_distinct:
            return i+1
    return -1

def solve_1(lines):
    return solve(lines,4)


def solve_2(lines):
    return solve(lines, 14)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))