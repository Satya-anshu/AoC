import os
import copy
import collections
import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def extract_info(lines):
    enhancement, img = lines.split('\n\n')
    enhancement = [1 if x == '#' else 0 for x in enhancement]
    img = [[1 if x == '#' else 0 for x in line] for line in img.split()]
    return enhancement,img

def solve(lines,steps):
    enhanced, img = extract_info(lines)
    val = [enhanced[0], enhanced[511] if enhanced[0] else enhanced[0]]
    mat = np.asarray(img)
    for step in range(steps):
        for i in range(3):
            mat = np.pad(mat,(1,1),mode="constant",constant_values=(val[(step+1)%2]))
        new_mat = np.zeros(shape=mat.shape).astype(np.int32)
        for i in range(len(mat)-2):
            for j in range(len(mat[0])-2):
                bits = [mat[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                index = int(''.join(map(str, bits)), 2)
                new_mat[i+1][j+1] = enhanced[index]
        mat = [line[2:-2] for line in new_mat[2:-2]]
        mat = np.asarray(mat)
    return np.count_nonzero(mat)

def solve_1(lines):
    print("Part 1: ",solve(lines,2))

def solve_2(lines):
    print("Part 2: ",solve(lines,50))

if __name__ == "__main__":
    lines = open("input.txt","r").read()
    linesTest = open("test.txt","r").read()
    solve_1(lines)
    solve_2(lines)