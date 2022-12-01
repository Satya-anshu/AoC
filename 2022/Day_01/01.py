import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

test_input = \
'''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

def solve_part1(lines):
    total = 0
    current_sum = 0
    for line in lines:
        if line == '':
            current_sum = 0
        else:
            current_sum += int(line)
            total = max(current_sum, total)
    print("Part 1: ", total)
    
def solve_part2(lines):
    total = []
    current_sum = 0
    for line in lines:
        if line == '':
            total.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
    total.sort()
    print("Part 2: ", sum(total[-3:]))

if __name__ == "__main__":
    lines = list(map(str,open("input.txt","r").read().splitlines()))
    linesTest = list(map(str,test_input.splitlines()))
    # Part 1
    solve_part1(lines)

    # Part 2
    solve_part2(lines)