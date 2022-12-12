import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''

def check(x):
    if x == 'S':
        return ord('a')
    elif x == 'E':
        return ord('z')
    else:
        return ord(x)

def solve(lines, part):
    rows, cols = len(lines), len(lines[0])
    
    start = tuple()
    dist = [[float('inf') for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == 'S':
                if part == 1:
                    start = (i,j)
                    dist[i][j] = 0
            elif lines[i][j] == 'E':
                if part == 2:
                    start = (i,j)
                    dist[i][j] = 0
    
    # Use BFS to find the shortest path from S to E
    q = collections.deque()
    q.append(start)
    while len(q) > 0:
        posx, posy = q.popleft()
        # Check all 4 directions
        for neigh in ((-1,0), (1,0), (0,-1), (0,1)):
            x,y = neigh
            new_posx = x + posx
            new_posy = y + posy
            # Safe to visit the new_posx
            if 0 <= new_posx < rows and 0 <= new_posy < cols:
                dst = lines[new_posx][new_posy]
                src = lines[posx][posy]

                if part == 1:
                    val = check(dst) - check(src)
                else:
                    val = check(src) - check(dst)
                
                if (val <= 1) and dist[new_posx][new_posy] > 1 + dist[posx][posy]:
                    dist[new_posx][new_posy] = dist[posx][posy] + 1
                    if (part == 1 and dst == 'E') or (part == 2 and dst in 'Sa'):
                        return dist[new_posx][new_posy]
                    else:
                        q.append((new_posx,new_posy))
    return None

def solve_1(lines):
    # Get min distance from 'S' to 'E'
    return solve(lines,1)

def solve_2(lines):
    # Get min distance from 'E' to (any 'a' or 'S')
    return solve(lines, 2)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))