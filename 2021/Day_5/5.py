import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''
class Line:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
def get_lines(lines):
    line_arr = []
    for line in lines:
        left,right = line.split("->")
        x1,y1 = map(int,left.split(","))
        x2,y2 = map(int,right.split(","))
        line_arr.append(Line(x1,y1,x2,y2))
    return line_arr

def print_intersection(line_map):
    cnt_intersection = 0
    for k,v in line_map.items():
        if v > 1:
            cnt_intersection+=1
    print(cnt_intersection)

def map_points(line_map,x1,y1,x2,y2,dx,dy):
    dx = 1 if dx > 0 else (0 if dx == 0 else -1)
    dy = 1 if dy > 0 else (0 if dy == 0 else -1)
    
    x,y = x1,y1
    while x != x2+dx or y != y2+dy:
        if (x,y) in line_map:
            line_map[(x,y)] += 1
        else:
            line_map[(x,y)] = 1
        x += dx
        y += dy

def solve_1(lines):
    lines = get_lines(lines)
    line_map = collections.defaultdict()
    for line in lines:
        if line.x1 == line.x2 or line.y1 == line.y2:
            map_points(line_map,line.x1,line.y1,line.x2,line.y2, line.x2-line.x1, line.y2-line.y1)

    print_intersection(line_map)


def solve_2(lines):
    lines = get_lines(lines)
    line_map = collections.defaultdict()
    for line in lines:
        map_points(line_map,line.x1,line.y1,line.x2,line.y2, line.x2-line.x1, line.y2-line.y1)

    print_intersection(line_map)
if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)