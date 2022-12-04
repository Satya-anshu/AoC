import os
import copy
import collections
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

def solve_1(lines):
    overlap = 0
    for line in lines:
        elf1,elf2 = line.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")

        start = min(int(elf1_start),int(elf2_start))
        end = max(int(elf1_end),int(elf2_end))

        range = str(start) + "-" + str(end)

        if range == elf1 or range == elf2:
            overlap += 1
    return overlap

def solve_2(lines):
    overlap = 0
    for line in lines:
        elf1,elf2 = line.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")

        if not(int(elf1_end) < int(elf2_start) or int(elf2_end) < int(elf1_start)):
            overlap += 1
    return overlap

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))