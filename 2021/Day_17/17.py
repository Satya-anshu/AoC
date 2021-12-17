import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''target area: x=20..30, y=-10..-5
'''
def extract_info(lines):
    info = lines[0].split(" ")[2:]
    x = info[0].split("=")[1]
    y = info[1].split("=")[1]
    x1,x2=x.split("..")
    x2 = x2[:-1]
    y1,y2=y.split("..")
    return map(int,[x1,x2,y1,y2])

def solve_1(lines):
    x1,x2,y1,y2 = extract_info(lines)
    
    low_x,low_y = min(x1,x2),min(y1,y2)
    high_x,high_y = max(x1,x2),max(y1,y2)
    ymax = -1
    for x in range(0,1000):
        for y in range(0,1000):
            launch_x = x
            launch_y = y
            yLocalMax = -1
            first = False
            while True:
                if not first:
                    pos = [launch_x,launch_y]
                    first = True
                else:
                    new_x = pos[0] + launch_x
                    new_y = pos[1] + launch_y
                    pos = [new_x,new_y]
                if launch_x > 0:
                    launch_x -= 1
                elif launch_x < 0:
                    launch_x += 1
                launch_y -= 1
                #print(launch_x,launch_y,pos)
                yLocalMax = max(yLocalMax,pos[1])
                if low_x <= pos[0] <= high_x and low_y <= pos[1] <= high_y:
                    ymax = max(ymax,yLocalMax)
                    break
                elif pos[0] > high_x or pos[1] < low_y:
                    break
    print(ymax)

def solve_2(lines):
    x1,x2,y1,y2 = extract_info(lines)
    low_x,low_y = min(x1,x2),min(y1,y2)
    high_x,high_y = max(x1,x2),max(y1,y2)
    ymax = -1
    cnt = 0
    for x in range(0,1000):
        for y in range(-1000,1000):
            launch_x = x
            launch_y = y
            yLocalMax = -1
            first = False
            while True:
                if not first:
                    pos = [launch_x,launch_y]
                    first = True
                else:
                    new_x = pos[0] + launch_x
                    new_y = pos[1] + launch_y
                    pos = [new_x,new_y]
                if launch_x > 0:
                    launch_x -= 1
                elif launch_x < 0:
                    launch_x += 1
                launch_y -= 1
                yLocalMax = max(yLocalMax,pos[1])
                if low_x <= pos[0] <= high_x and low_y <= pos[1] <= high_y:
                    ymax = max(ymax,yLocalMax)
                    cnt+=1
                    break
                elif pos[0] > high_x or pos[1] < low_y:
                    break
    print(cnt)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)