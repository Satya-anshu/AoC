import os
import copy
import collections
import pytest

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''
'''

def solve_1(lines):
    for line in lines:
        pass
    return 0

def solve_2(lines):
    for line in lines:
        pass
    return 0

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (test_input, 0),
    ),
)
def test(input_s, expected):
    assert(solve_1(input_s) == expected)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))