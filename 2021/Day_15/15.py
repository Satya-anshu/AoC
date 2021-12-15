import os
import copy
import collections
import numpy as np
import heapq as pq

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''

def search(m):
    h,w = np.shape(m)
    q = [(0,(0,0))]     # risk, starting point
    while q:
        risk, (x,y) = pq.heappop(q)
        if (x,y) == (w-1,h-1):
            return risk
        for x,y in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
            if x >= 0 and x < w and y >= 0 and y < h and m[y][x] >= 0:
                pq.heappush(q, (risk+(m[y][x] % 9)+1, (x,y)))
                m[y][x] = -1    # mark as seen

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    grid = [[0]*len(lines)]*len(lines)
    temp = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            grid[i][j] = int(lines[i][j])
        temp.append(copy.deepcopy(grid[i]))
    
    lines = np.array(temp, dtype=int) - 1
    print("Part 1: ",search(lines.copy()))
    lines = np.concatenate([lines+i for i in range(5)],axis=0)
    lines = np.concatenate([lines+i for i in range(5)],axis=1)
    print("Part 2:",search(lines))
