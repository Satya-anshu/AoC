import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
def find_priority_sum(commons):
    sum = 0
    for c in commons:
        if c >= 'a' and c <= 'z':
            sum += ord(c) - ord('a') + 1
        else:
            sum += ord(c) - ord('A') + 27
    return sum

def solve_1(lines):
    commons = []
    for line in lines:
        common_set = set(line[len(line)//2 :]).intersection(set(line[:len(line)//2]))
        commons.append(common_set.pop())
    return find_priority_sum(commons)

def solve_2(lines):
    commons = []
    for i in range(0,len(lines),3):
        sack1, sack2, sack3 = set(lines[i]), set(lines[i+1]), set(lines[i+2])
        common_set = sack1.intersection(sack2).intersection(sack3)
        commons.append(common_set.pop())
    return find_priority_sum(commons)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))