lines = open('in.txt','r').readlines()
memory = {}
for line in lines:
    line = line.strip(' \n').split(' ')
    if 'mask' in line:
        mask = line[-1]
    else:
        mem = int(line[0][4:-1])
        val = int(line[-1])
        binVal = bin(val)[2:]
        for i in range(len(binVal),36):
            binVal = '0' + binVal
        afterMaskVal = ['0' for i in range(36)]
        for i in range(36):
            if mask[i] != 'X':
                afterMaskVal[i] = mask[i]
            else:
                afterMaskVal[i] =  binVal[i]
        memory[mem] = int(''.join(afterMaskVal),2)
print("Part 1: ", sum(memory.values()))
    
