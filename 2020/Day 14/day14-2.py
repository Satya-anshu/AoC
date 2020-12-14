lines = open('in.txt','r').readlines()
memory = {}
def findX(actual,memory, V):
    count = actual.count('X')
    for i in range(2**count):
        val = bin(i)[2:]
        for i in range(len(val),count):
            val = '0' + val
        ctr = 0
        temp = actual.copy()
        for j in range(36):
            if temp[j] == 'X':
                temp[j] = val[ctr]
                ctr+=1
        memory[int(''.join(temp),2)] = V
for line in lines:
    line = line.strip(' \n').split(' ')
    if 'mask' in line:
        mask = line[-1]
    else:
        mem = int(line[0][4:-1])
        val = int(line[-1])
        binVal = bin(mem)[2:]
        for i in range(len(binVal),36):
            binVal = '0' + binVal
        afterMaskVal = ['0' for i in range(36)]
        for i in range(36):
            if mask[i] == 'X' or mask[i] == '1':
                afterMaskVal[i] = mask[i]
            else:
                afterMaskVal[i] =  binVal[i]
        findX(afterMaskVal,memory, val)
print("Part 2: ", sum(memory.values()))
    
