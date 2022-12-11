import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''
def parse(lines):
    items = []
    operations = []
    div = []
    true = []
    false = []
    idx = -1
    for line in lines:
        line_token = line.split(" ")
        if len(line_token) == 1:
            continue
        if line_token[0] == "Monkey":
            idx = line_token[1].split(":")[0]
        elif line_token[2] == "Starting":
            holding = line_token[4:]
            get_items = []
            for h in holding:
                i = h.split(",")[0]
                get_items.append(int(i))
            items.append(get_items)
        elif line_token[2] == "Operation:":
            operation = line_token[5:]
            operations.append(operation)
        elif line_token[2] == "Test:":
            div.append(int(line_token[5]))
        elif line_token[5] == "true:":
            true.append(int(line_token[9]))
        elif line_token[5] == "false:":
            false.append(int(line_token[9]))
        else:
            continue
    return items, operations, div, true, false

def solve(lines, part, rounds):
    items,operations,div,true,false = parse(lines)
    items_queue = [collections.deque() for i in range(len(items))]
    for i in range(len(items)):
        for it in items[i]:
            items_queue[i].append(it)
    
    super_mod = 1
    for d in div:
        super_mod = super_mod * d
    
    inspection = [0 for i in range(len(items))]
    for _ in range(rounds):
    
        # For each round, play this game
        for i in range(len(items_queue)):
            # Play the game!
            # For every item, do the operation, monkey gets bored -> // 3, throw to next_monkey
            while len(items_queue[i]) > 0:
                item = items_queue[i].popleft()
                inspection[i] += 1
                worry = 0
                if operations[i][1] == '+':
                    if operations[i][2] == 'old':
                        worry = item + item
                    else:
                        worry = item + int(operations[i][2])
                else:
                    if operations[i][2] == 'old':
                        worry = item * item
                    else:
                        worry = item * int(operations[i][2])
                
                # Now monkey gets bored
                if part == 1:
                    worry = worry // 3
                else:
                    worry = worry % super_mod

                # Check divisibility and throw item away
                if worry % div[i] == 0:
                    new_monkey_idx = true[i]
                    items_queue[new_monkey_idx].append(worry)
                else:
                    new_monkey_idx = false[i]
                    items_queue[new_monkey_idx].append(worry)
    
    inspection.sort(reverse=True)
    return inspection[0]*inspection[1]

def solve_1(lines, part, rounds):
    return solve(lines, part, rounds)

def solve_2(lines, part, rounds):
    return solve(lines, part, rounds)

if __name__ == "__main__":
    lines = open("input.txt","r").read().split("\n")
    linesTest = test_input.split("\n")
    print('Part 1: ',solve_1(lines, 1, 20))
    print('Part 2: ',solve_2(lines, 2, 10000))