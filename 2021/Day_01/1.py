import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''199
200
208
210
200
207
240
269
260
263
'''
def solve_part1(lines):
    curr, prev = -1,-1
    ans = 0
    for line in lines:
        curr = line
        if prev == -1:
            prev = curr
            continue
        if curr > prev:
            ans+=1
        prev = curr
    print(ans)

def solve_part2(lines):
    curr,prev = -1,-1
    sum = 0
    ans = 0
    for i,val in enumerate(lines):
        sum += val
        if i < 2:
            continue
        if i > 2:
            sum -= lines[i-3]
        curr = sum
        if prev == -1:
            prev = curr
            continue
        if curr > prev:
            ans+=1
        prev = curr
    print(ans)

if __name__ == "__main__":
    lines = list(map(int,open("input.txt","r").read().splitlines()))
    linesTest = list(map(int,test_input.splitlines()))
    # Part 1
    solve_part1(lines)

    # Part 2
    solve_part2(lines)