import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''
def addX(X,val):
    return X + val

signal_strength = (20,60,100,140,180,220)
def solve_1(lines):
    cycle = 0
    X = 1
    ans = 0
    for line in lines:
        if line == "noop":
            cycle += 1
            if cycle in signal_strength:
                ans += X * cycle
        else:
            val = int(line.split(" ")[1])
            cycle += 1
            if cycle in signal_strength:
                ans += X * cycle
            cycle += 1
            if cycle in signal_strength:
                ans += X * cycle
            X = addX(X,val)
    return ans

def print_crt(crt_pos, sprite_pos):
    if crt_pos in (sprite_pos - 1, sprite_pos, sprite_pos + 1):
        print("#", end = "") #@,!,. also give some clear shapes :-)
    else:
        print(" ", end = "")
    return crt_pos + 1

def solve_2(lines):
    crt_pos = 0
    sprite_pos = 1
    cycle = 0
    for line in lines:
        if line == "noop":
            crt_pos = print_crt(crt_pos, sprite_pos)
            cycle += 1
            if cycle % 40 == 0:
                print()
                crt_pos = 0
        else:
            val = int(line.split(" ")[1])
            crt_pos = print_crt(crt_pos, sprite_pos)
            cycle += 1
            if cycle % 40 == 0:
                print()
                crt_pos = 0
            crt_pos = print_crt(crt_pos, sprite_pos)
            cycle += 1
            if cycle % 40 == 0:
                print()
                crt_pos = 0
            sprite_pos += val

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines)) #BPJAZGAP