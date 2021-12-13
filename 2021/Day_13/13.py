import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''
def fold_y(y, mat):
    folded_mat = copy.deepcopy(mat)
    for _x,_y in mat:
        if _y > y:
            new_x = _x
            new_y = y - (_y - y)
            folded_mat.remove((_x,_y))
            folded_mat.add((new_x,new_y))
        elif _y == y:
            folded_mat.remove((_x,_y))
    return folded_mat

def fold_x(x, mat):
    folded_mat = copy.deepcopy(mat)
    for _x,_y in mat:
        if _x > x:
            new_x = x - (_x - x)
            new_y = _y
            folded_mat.remove((_x,_y))
            folded_mat.add((new_x,new_y))
        elif _x == x:
            folded_mat.remove((_x,_y))
    return folded_mat

def extract_info(lines):
    ins = []
    mat = set()
    start_ins = False
    for line in lines:
        if line == '':
            start_ins = True
            continue
        else:
            if not start_ins:
                x,y = map(int,line.split(","))
                mat.add((x,y))
            else:
                ins.append(line.split(" ")[2])
    return mat,ins

def solve_1(lines):
    mat,instructs = extract_info(lines)
    for ins in instructs:
        char,val = ins.split("=")
        if char == 'x':
            mat = fold_x(int(val),mat)
        else:
            mat = fold_y(int(val),mat)
        break
    print(len(mat))


def solve_2(lines):
    mat,instructs = extract_info(lines)
    for ins in instructs:
        char,val = ins.split("=")
        if char == 'x':
            mat = fold_x(int(val),mat)
        else:
            mat = fold_y(int(val),mat)
    max_x,max_y = -1,-1
    for x,y in mat:
        max_x = max(x,max_x)
        max_y = max(y,max_y)
    
    grid = [[' '] * (max_x+1) for i in range(max_y+1)]
    for (x,y) in mat:
        grid[y][x] = '#'
    for g in grid:
        print(g)
    #Ans = RHALRCRA

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)