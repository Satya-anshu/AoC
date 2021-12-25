import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import re
def solve(lines):
    return sum([int(n) for n in re.findall('-?[0-9]+', lines)])

if __name__ == "__main__":
    print('Part 1: ',solve(open("input.txt").read()))
    #print('Part 2: ',next_password(next_password("vzbxkghb")))