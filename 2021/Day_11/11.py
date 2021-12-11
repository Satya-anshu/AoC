import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

def solve_1(lines,steps):
    total_flashes = 0
    safe = lambda a,b: 0<=a<len(lines) and 0<=b<len(lines[0])
    for step in range(steps):
        q = collections.deque()
        for row,line in enumerate(lines):
            for col,val in enumerate(line):
                lines[row][col] += 1
                if lines[row][col] == 10:
                    q.append((row,col))
        
        while len(q) > 0:
            row,col = q.popleft()
            for pos_x in range(-1,2):
                for pos_y in range(-1,2):
                    if pos_x == pos_y == 0:
                        continue
                    new_x = row + pos_x
                    new_y = col + pos_y
                    if safe(new_x,new_y):
                        lines[new_x][new_y] += 1
                        if lines[new_x][new_y] == 10:
                            q.append((new_x,new_y))
                            
        # Find and reset all flashes
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] > 9:
                    lines[i][j] = 0
                    total_flashes+=1
    print(total_flashes)

def solve_2(lines):
    safe = lambda a,b: 0<=a<len(lines) and 0<=b<len(lines[0])
    steps = 1
    while True:
        q = collections.deque()
        flashed = set()
        for row,line in enumerate(lines):
            for col,val in enumerate(line):
                lines[row][col] += 1
                if lines[row][col] == 10:
                    q.append((row,col))
                    flashed.add((row,col))
        
        while len(q) > 0:
            row,col = q.popleft()
            for pos_x in range(-1,2):
                for pos_y in range(-1,2):
                    if pos_x == pos_y == 0:
                        continue
                    new_x = row + pos_x
                    new_y = col + pos_y
                    if safe(new_x,new_y):
                        lines[new_x][new_y] += 1
                        if lines[new_x][new_y] == 10:
                            q.append((new_x,new_y))
        cnt = 0
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] > 9:
                    lines[i][j] = 0
                    cnt += 1
        if cnt == len(lines) * len(lines[0]):
            print(steps)
            return
        steps += 1

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    part1 = [list(map(int,list(line))) for line in lines]
    part2 = [list(map(int,list(line))) for line in lines]
    solve_1(part1,100)
    solve_2(part2)