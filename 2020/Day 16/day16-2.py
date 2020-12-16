lines = open('in.txt','r').read().splitlines()
valid_numbers = set()
valid_data = {}
invalid_sum = 0
other = False
my_ticket = []
valid_tickets = []
your = False
for line in lines:
    if "nearby" in line:
        other = True
    elif other == True:
        nums = line.split(',')
        invalid = False
        for i in nums:
            if int(i) not in valid_numbers:
                invalid = True
        if not invalid:
            valid_tickets.append(nums)
    elif line == '':
        pass
    elif "your" in line:
        your = True
    elif your == True:
        my_ticket = line.split(',')
        your = False
    else:
        values = line.split(' ')
        s = ''
        for v in values:
            if '-' in v:
                ns = v.split('-')
                low = int(ns[0])
                high = int(ns[1])
                if s not in valid_data:
                    valid_data[s] = set()
                for x in range(low,high+1):
                    valid_data[s].add(x)
                    valid_numbers.add(x)
            elif 'or' in v:
                pass
            else:
                s = s + v
'''
Parsing is done till here

Idea:
For every entry in key, find all the dictionary items which are valid
There will be exactly one key pertaining in the final array, remove all instances of this and repeat again till we find all possible matches
Done!
'''
actual_set = []
for i in range(len(valid_tickets[0])):
    cur_idx = i
    for k,v in valid_data.items():
        can_be = 0
        for j in range(len(valid_tickets)):
            if int(valid_tickets[j][i]) in v:
                can_be += 1
        if can_be == len(valid_tickets):
            actual_set.append([k,i])
ans = 1
#Dep = 6
#Class = 12, ALoc = 9, Atrack = 7
final_set = []
while True:
    count = {}
    cur_val = 0
    for i in range(len(actual_set)):
        if actual_set[i][1] in count:
            count[actual_set[i][1]] += 1
        else:
            count[actual_set[i][1]] = 1
    #COunt
    for k,v in count.items():
        if v == 1:
            #For which key?
            for i in range(len(actual_set)):
                if actual_set[i][1] == k:
                    final_set.append([actual_set[i][0],k])
                    break
            #Remove entries with key match
            for i in range(20):
                if [final_set[-1][0],i] in actual_set:
                    actual_set.remove([final_set[-1][0],i])
    if actual_set == []:
        break

ids = [i[1] for i in final_set if "depart" in i[0]]
for id in ids:
    ans = ans * int(my_ticket[id])
print("Part 2: ", ans)
        
