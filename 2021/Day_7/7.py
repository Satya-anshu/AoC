import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''16,1,2,0,4,2,7,1,2,14
'''
def solve_1(pos):
    pos.sort()
    size = len(pos)
    mid, mid1, mid2 = 0,0,0
    # print(pos,size)
    if size % 2 == 1:
        mid = pos[size//2]
        print(sum([abs(i-mid) for i in pos]))
    else:
        mid1 = pos[size//2]
        mid2 = pos[size//2 -1]
        sum1 = sum([abs(i-mid1) for i in pos])
        sum2 = sum([abs(i-mid2) for i in pos])
        print(min(sum1,sum2))

def solve_2(pos):
    min_pos = min(pos)
    max_pos = max(pos)
    # For each pos, calculate how much fuel it costs for crabs
    ans = 10**18
    for i in range(min_pos,max_pos+1):
        fuel_cost = 0
        for p in pos:
            diff = abs(p-i)
            cost = (diff * (diff+1))//2
            fuel_cost += cost
        ans = min(ans,fuel_cost)
    print(ans)

if __name__ == "__main__":
    lines = list(map(int,open("input.txt","r").read().splitlines()[0].split(",")))
    linesTest = list(map(int,test_input.splitlines()[0].split(",")))
    solve_1(lines)
    solve_2(lines)