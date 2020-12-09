lines = open('input.txt','r').readlines()
num = [int(line) for line in lines]

preamble = 25
invalidNum = 0
for i in range(preamble, len(num)): #Preamble length...initial loading
    currNum = num[i]
    found = False
    #Check if any of the prev numbers sum to this number
    for j in range(i - preamble, i):
        for k in range(j-preamble + 1, i):
            #print(k)
            if num[j] + num[k] == currNum:
                found = True
    if not found:
        invalidNum = currNum
        print("Part 1: ", currNum)
        break

'''Find contiguous list of numbers which sum to given larger number'''
contSet = []
i = 0
while i < len(num):
    if sum(contSet) < invalidNum:
        contSet.append(num[i])
        i += 1
    elif sum(contSet) == invalidNum:
        #print(contSet)
        print("Part 2: ", min(contSet) + max(contSet))
        break
    else:
        while sum(contSet) > invalidNum:
            contSet = contSet[1:]
    #print(contSet)
