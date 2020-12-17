lines = open('in.txt','r').read().splitlines()
num = [int(line) for line in lines]

def part1_find_two(num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                print ("Part 1: ", num[i] * num[j])
                return

def part2_find_three(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                if num[i] + num[j] + num[k] == target:
                    print("Part 2: ", num[i]* num[j] * num[k])
                    return

part1_find_two(num,2020)
part2_find_three(num,2020)
