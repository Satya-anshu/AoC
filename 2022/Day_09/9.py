import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

test_input2 = \
'''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

def move(ptr, dir):
    if dir == 'L':
        ptr[0] = ptr[0] - 1
    elif dir == 'R':
        ptr[0] = ptr[0] + 1
    elif dir == 'U':
        ptr[1] = ptr[1] + 1
    elif dir == 'D':
        ptr[1] = ptr[1] - 1

def is_touching(head, tail):
    if abs(head[0]-tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return True
    else:
        return False

def get_next_tail_location(head, tail):
    if is_touching(head,tail):
        return tail
    # Same X-axis    
    if head[0] == tail[0]:
        new_tail = [tail[0], (head[1] + tail[1]) // 2]
        return new_tail
    
    # Same Y-axis
    if head[1] == tail[1]:
        new_tail = [(head[0] + tail[0]) // 2, tail[1]]
        return new_tail
    
    # Diagonal move
    for neigh in ((-1,-1),(-1,1),(1,-1),(1,1)):
        possible = [tail[0]+neigh[0], tail[1] + neigh[1]]
        if is_touching(head, possible):
            return possible

def solve(lines, knots):
    vis = set()
    rope = []
    for i in range(knots):
        rope.append([0,0])
    
    for line in lines:
        dir, steps = line.split(" ")
        steps = int(steps)
        for s in range(steps):
            move(rope[0],dir)
            for i in range(1, len(rope)):
                rope[i] = get_next_tail_location(rope[i-1],rope[i])
            vis.add((rope[-1][0],rope[-1][1]))
    return len(vis)

def solve_1(lines):
    return solve(lines,2)

def solve_2(lines):
    return solve(lines,10)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input2.splitlines()
    print('Part 1: ',solve_1(lines))
    print('Part 2: ',solve_2(lines))