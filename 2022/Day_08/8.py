import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''30373
25512
65332
33549
35390
'''
def parse(lines):
    mat = [[]]
    for line in lines:
        for n in line:
            mat[-1].append(int(n))
        mat.append([])
    mat.pop()

    rows, cols = len(mat),len(mat[0])
    vis = [[False for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            if (i in (0,rows-1)) or (j in (0,cols-1)):
                vis[i][j] = True
    
    # Check left to right
    for i in range(1, rows-1):
        max_so_far = mat[i][0]
        for j in range(1, cols-1):
            if mat[i][j] > max_so_far:
                vis[i][j] = True
                max_so_far = mat[i][j]
   
    # Check right to left
    for i in range(1, rows-1):
        max_so_far = mat[i][cols-1]
        for j in range(cols-2, 0, -1):
            if mat[i][j] > max_so_far:
                vis[i][j] = True
                max_so_far = mat[i][j]

    # Check top to down
    for j in range(1, cols-1):
        max_so_far = mat[0][j]
        for i in range(1, rows-1):
            if mat[i][j] > max_so_far:
                vis[i][j] = True
                max_so_far = mat[i][j]
    
    # Check bot to top
    for j in range(1, cols-1):
        max_so_far = mat[rows-1][j]
        for i in range(rows-2, 0,-1):
            if mat[i][j] > max_so_far:
                vis[i][j] = True
                max_so_far = mat[i][j]
    
    return vis, mat

def solve_1(lines):
    vis,mat = parse(lines)
    ans = 0
    for i in vis:
        for j in i:
            if j:
                ans += 1
    return ans


def scenic_score(mat, r, c):
    rows,cols = len(mat),len(mat[0])
    score = 1
    for d in ((-1,0),(1,0),(0,-1),(0,1)):
        x,y = d
        dir_score = 0
        while 0 <= r + x < rows and 0 <= c + y < cols:
            if mat[r][c] > mat[r+x][c+y]:
                # My height is greater
                dir_score += 1
            else:
                # Stop since height is equal or greater than me
                dir_score += 1
                break

            if x < 0:
                x -= 1
            elif x > 0:
                x += 1
            
            if y > 0:
                y += 1
            elif y < 0:
                y -= 1
        
        score *= dir_score

    return score

def solve_2(lines):
    vis,mat = parse(lines)
    rows, cols = len(mat), len(mat[0])
    ans = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if vis[i][j]:
                # Find the scenic score for this
                ans = max(ans, scenic_score(mat,i,j))
    return ans

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))