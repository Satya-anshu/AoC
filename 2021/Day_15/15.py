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

def search(chiton):
    h,w = np.shape(chiton)
    q = [(0,(0,0))]     # (risk and starting points for chiton)
    while q:
        risk, (x,y) = pq.heappop(q)
        if (x,y) == (w-1,h-1):
            return risk
        for x,y in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
            # The way grid is given, it should be traversed in y,x fashion
            if 0 <= x < w and 0 <= y < h and chiton[y][x] >= 0:
                pq.heappush(q, (risk+(chiton[y][x] % 9)+1, (x,y)))
                # Mark chiton as visited
                chiton[y][x] = -1

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()

    # There should be an easier way to handle this mess
    grid = [[0]*len(lines)]*len(lines)
    temp = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            grid[i][j] = int(lines[i][j])
        temp.append(copy.deepcopy(grid[i]))
    
    lines = np.array(temp, dtype=int) - 1
    # Yeah seriously, need to find a better and more elegant way

    print("Part 1: ",search(lines.copy()))

    # Cool numpy trick I wanted to exploit after going through hamsterz0's ;) code!
    lines = np.concatenate([lines+i for i in range(5)],axis=0)
    lines = np.concatenate([lines+i for i in range(5)],axis=1)
    print("Part 2:",search(lines))
    