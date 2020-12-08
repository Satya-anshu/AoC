class Ins:
    def __init__(self, name,val,run):
        self.name = name
        self.val = int(val)
        self.run = run

def Run(ins):
    acc = 0
    ctr = 0
    prev_ctr = 0
    for i in range(len(ins)):
        ins[i].run = 0
    
    while ctr < len(ins):
        ins[ctr].run += 1
        if ins[ctr].run == 2:
            return True,acc
        prev_ctr = ctr
        name = ins[ctr].name
        if name == 'nop':
            ctr += 1
        elif name == 'acc':
            acc += ins[ctr].val
            ctr += 1
        else:
            ctr += ins[ctr].val
    return False, acc

lines = open('input.txt','r').readlines()
ins = []
for i in range(len(lines)):
    line = lines[i].strip('\n').split(' ')
    ins.append(Ins(line[0],int(line[1]),0))

success, acc = Run(ins)
print("Part1: ",acc)

acc = 0
for i in range(len(ins)):
    if ins[i].name == 'nop' or ins[i].name == 'jmp':
        ins[i].name = 'nop' if ins[i].name == 'jmp' else 'jmp'
        succ,acc = Run(ins)
        if not succ:
            print("Part 2: ",acc)
            break
        ins[i].name = 'nop' if ins[i].name == 'jmp' else 'jmp'
