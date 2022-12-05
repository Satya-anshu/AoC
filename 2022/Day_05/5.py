import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''
'''
def parse(lines):
    # My input
    stacks = [
        'DLJRVGF',
        'TPMBVHJS',
        'VHMFDGPC',
        'MDPNGQ',
        'JLHNF',
        'NFVQDGTZ',
        'FDBL',
        'MJBSVDN',
        'GLD'
    ]
    stacks = [list(s) for s in stacks]
    return stacks

def solve(lines, use_stack_ordering):
    stacks = parse(lines)
    for line in range(10,len(lines)):
        ins = lines[line].split(" ")
        stacks_to_move = int(ins[1])
        from_stack = int(ins[3]) - 1
        to_stack = int(ins[5]) - 1
        if use_stack_ordering == True:
            for _ in range(stacks_to_move):
                s = stacks[from_stack].pop()
                stacks[to_stack].append(s)
        else:
            order = []
            for _ in range(stacks_to_move):
                s = stacks[from_stack].pop()
                order.append(s)
            order.reverse()
            for o in order:
                stacks[to_stack].append(o)
    ans = []
    for s in stacks:
        ans.append(s[-1])
    return ''.join(ans)

def solve_1(lines):
    return solve(lines, True)

def solve_2(lines):
    return solve(lines, False)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))