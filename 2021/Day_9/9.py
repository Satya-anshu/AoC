import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''2199943210
3987894921
9856789892
8767896789
9899965678
'''
dirs_4=[[0,-1],[0,1],[1,0],[-1,0]]

def get_low_pts(lines):
    low_pts = []
    safe = lambda a,b: 0<=a<len(lines) and 0<=b<len(lines[0])
    for row,line in enumerate(lines):
        for col, num in enumerate(line):
            # Find adjacent numbers in 4 directions
            vals = []
            for dir in dirs_4:
                dx = row + dir[0]
                dy = col + dir[1]
                if safe(dx,dy):
                    vals.append(int(lines[dx][dy]))
            not_found = False
            for v in vals:
                if int(num) >= v:
                    not_found = True
            if not_found:
                continue
            else:
                low_pts.append([int(num), row, col])
    return low_pts

def solve_1(lines):
    low_pts = get_low_pts(lines)
    sum = 0
    for num in low_pts:
        sum += num[0]+1
    print(sum)

def solve_2(lines):
    low_pts = get_low_pts(lines)
    basins = []
    # For every low point, do BFS, ignore 9
    safe = lambda a,b: 0<=a<len(lines) and 0<=b<len(lines[0])
    for pt in low_pts:
        q = collections.deque()
        q.append((pt[0],pt[1],pt[2]))
        vis = set()
        basin_size = 0
        while len(q) > 0:
            v,x,y = q.popleft()
            basin_size += 1
            for dir in dirs_4:
                new_x = x + dir[0]
                new_y = y + dir[1]
                if safe(new_x,new_y) and lines[new_x][new_y] > str(v) and lines[new_x][new_y] != '9' and (new_x,new_y) not in vis:
                    vis.add((new_x,new_y))
                    q.append((lines[new_x][new_y],new_x,new_y))
        basins.append(basin_size)
    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)