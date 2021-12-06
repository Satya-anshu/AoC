import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''3,4,3,1,2
'''
def solve_1(lines):
    days_left = [0] * 9
    total = 0
    for day in lines:
        days_left[day] += 1

    total = sum(days_left)

    for day in range(80):
        total += days_left[0]
        carry = days_left[0]
        for i in range(len(days_left)-1):
            days_left[i] = days_left[i+1]
        days_left[6] += carry
        days_left[8] = carry
    print(total)

def solve_2(lines):
    # Here the exponential growth would kill the processing
    # Need an efficient way to handle it.
    # Any new fish that gets created starts from 8 and older ones start from 7
    # Let's have an array to keep count of fishes of current days..and see how many new ones they spawn off
    days_left = [0] * 9
    total = 0
    for day in lines:
        days_left[day] += 1

    total = sum(days_left)

    for day in range(256):
        total += days_left[0]
        carry = days_left[0]
        for i in range(len(days_left)-1):
            days_left[i] = days_left[i+1]
        days_left[6] += carry
        days_left[8] = carry
    print(total)

if __name__ == "__main__":
    lines = list(map(int,open("input.txt","r").read().splitlines()[0].split(",")))
    linesTest = list(map(int,test_input.splitlines()[0].split(",")))
    solve_1(lines)
    solve_2(lines)