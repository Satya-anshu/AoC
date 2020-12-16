lines = open('in.txt','r').read().splitlines()
valid_numbers = set()
invalid_sum = 0
other = False
my_ticket = []
for line in lines:
    if "nearby" in line:
        other = True
    elif other == True:
        nums = line.split(',')
        for i in nums:
            if int(i) not in valid_numbers:
                invalid_sum += int(i)
    elif line == '':
        pass
    elif "your" in line:
        my_ticket = line.split(',')
    else:
        values = line.split(' ')
        for v in values:
            if '-' in v:
                ns = v.split('-')
                low = int(ns[0])
                high = int(ns[1])
                for x in range(low,high+1):
                    valid_numbers.add(x)
print("Part 1: ", invalid_sum)
