from collections import defaultdict
num = [1,20,8,12,0,14]
spoken = defaultdict()
for i in range(len(num)):
    spoken[num[i]] = [i+1]

for i in range(len(num),2020):
    if len(spoken[num[i-1]]) == 1:
        num.append(0)
        if 0 in spoken:
            spoken[0].append(i+1)
        else:
            spoken[0] = [i+1]
    else:
        diff = spoken[num[i-1]][-1] - spoken[num[i-1]][-2]
        num.append(diff)
        if diff in spoken:
            spoken[diff].append(i+1)
        else:
            spoken[diff] = [i+1]
            
print(num[-1])
    
