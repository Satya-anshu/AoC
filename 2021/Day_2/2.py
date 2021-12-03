import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
def solve1(lines):
    x = 0
    y = 0
    for line in lines:
        ins,val = line.split()
        if "forward" in ins:
            x += int(val)
        elif "down" in ins:
            y += int(val)
        else:
            y -= int(val)
    print(x*y)

def solve2(lines):
    x = 0
    y = 0
    aim = 0
    for line in lines:
        ins,val = line.split()
        if "forward" in ins:
            x += int(val)
            y += aim * int(val)
        elif "down" in ins:
            aim += int(val)
        else:
            aim -= int(val)
    print(x*y)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = list(test_input.splitlines())
    #solve1(lines)
    solve2(lines)