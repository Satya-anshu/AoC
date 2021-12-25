import os
import itertools

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''

def solve(lines):
    grid = [line.strip() for line in lines]

    h, w = len(grid), len(grid[0])
    d = {(i,j): c for i, row in enumerate(grid) for j, c in enumerate(row) if c != '.'}

    for t in itertools.count(1):
        d1 = {p if c == '>' and (p:= (i, (j+1) % w)) not in d else (i,j): c for (i,j), c in d.items()}
        d1 = {p if c == 'v' and (p:= ((i+1) % h, j)) not in d1 else (i,j): c for (i,j),c in d1.items()}
        if d1 == d:
            return t
        d = d1
if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    print('Part 1: ',solve(lines))