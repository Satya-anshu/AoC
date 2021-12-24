import os
import copy
import collections
import pytest
import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''
'''
def parse(lines):
    instructions = set()
    wires = {}
    for line in lines:
        tokens = line.split()
        if len(tokens) == 5:
            instructions.add((tokens[4], tokens[0],tokens[1],tokens[2]))
        elif len(tokens) == 3:
            if tokens[0].isdigit():
                wires[tokens[2]] = int(tokens[0])
            else:
                instructions.add((tokens[2],tokens[0]))
        else:
            instructions.add((tokens[3], tokens[0],tokens[1]))
    
    return instructions,wires

def solve_1(lines):
    ins,wires = parse(lines)
    while ins:
        found = False
        for i in tuple(ins):
            if len(i) == 4:
                if (i[1] in wires or i[1].isdigit()) and (i[3] in wires or i[3].isdigit()):
                    if i[2] == 'AND':
                        wires[i[0]] = (wires[i[1]] if i[1] in wires else int(i[1])) & (wires[i[3]] if i[3] in wires else int(i[3]))
                    elif i[2] == 'OR':
                        wires[i[0]] = (wires[i[1]] if i[1] in wires else int(i[1])) | (wires[i[3]] if i[3] in wires else int(i[3]))
                    elif i[2] == 'LSHIFT':
                        wires[i[0]] = (wires[i[1]] if i[1] in wires else int(i[1])) << (wires[i[3]] if i[3] in wires else int(i[3]))
                    else:
                        wires[i[0]] = (wires[i[1]] if i[1] in wires else int(i[1])) >> (wires[i[3]] if i[3] in wires else int(i[3]))
                    ins.remove(i)
                    
            if len(i) == 2:
                if i[1] in wires:
                    wires[i[0]] = int(wires[i[1]])
                    ins.remove(i)
                    
            if len(i) == 3 and i[1] == 'NOT' and i[2] in wires:
                wires[i[0]] = 65335 - wires[i[2]]
                ins.remove(i)
                
    return wires['a']

def solve_2(lines):
    ins,wires = parse(lines)
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