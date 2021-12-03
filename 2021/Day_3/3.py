import os
from collections import defaultdict
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''
def solve_1(lines):
    # This is a matrix
    cntOnes = [0 for i in range(len(lines[0]))]
    numRows = len(lines)

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '1':
                cntOnes[j] += 1
    # print(cntOnes)
    # Build epsilon and gamma
    epsilon = 0
    gamma = 0
    for i,ones in enumerate(cntOnes):
        if max(ones,numRows-ones) == ones:
            gamma += (pow(2,len(cntOnes)-i-1))
        else:
            epsilon += (pow(2,len(cntOnes)-i-1))
    print(gamma * epsilon)

def filter(pos,oxygen,co2):
    # Count number of 0s and 1s for specified position and filter the list
    oxygenOnes = []
    oxygenZeros = []
    co2Ones = []
    co2Zeros = []
    if(len(oxygen) > 1):
        for i in range(len(oxygen)):
            if oxygen[i][pos] == '1':
                oxygenOnes.append(oxygen[i])
            else:
                oxygenZeros.append(oxygen[i])
    if (len(co2) > 1):
        for i in range(len(co2)):
            if co2[i][pos] == '1':
                co2Ones.append(co2[i])
            else:
                co2Zeros.append(co2[i])
    if(len(oxygenOnes) > 0 and len(oxygenZeros) > 0):
        if(len(oxygenOnes) >= len(oxygenZeros)):
            oxygen = oxygenOnes
        else:
            oxygen = oxygenZeros
    if(len(co2Ones) > 0 and len(co2Ones) > 0):
        if(len(co2Ones) >= len(co2Zeros) and len(co2Zeros) > 0):
            co2 = co2Zeros
        else:
            co2 = co2Ones
    return oxygen,co2

def solve_2(lines):
    # This is a matrix but we need the numbers here
    onesAtPos0 = []
    zerosAtPos0 = []
    for i in range(len(lines)):
        if lines[i][0] == '1':
            onesAtPos0.append(lines[i])
        else:
            zerosAtPos0.append(lines[i])
    
    if (len(onesAtPos0) > len(zerosAtPos0)):
        oxygen = onesAtPos0
        co2 = zerosAtPos0
    else:
        oxygen = zerosAtPos0
        co2 = onesAtPos0
    
    # Start filtering...
    for i in range(1,len(lines[0])):
        oxygen,co2 = filter(i,oxygen,co2)
        # print("After filtering at pos ",i)
        # print("Oxygen = ",oxygen)
        # print("Co2 = ",co2)
    
    print(int(oxygen[0],2) * int(co2[0],2))
if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)