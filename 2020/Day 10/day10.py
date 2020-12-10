lines = open('input.txt','r').readlines()
num = [int(i) for i in lines]
num.append(0)
highest = max(num) + 3
num.append(highest)
num.sort()
diff1 = 0
diff3 = 0
for i in range(len(num)-1):
    if num[i+1] - num[i] == 1:
        diff1+=1
    elif num[i+1] - num[i] == 3:
        diff3+=1
print("Part 1: ", diff1 * diff3)

#Part 2
'''
Tribonacci
'''
dp = [0 for i in range(10)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

diff = [num[i+1] - num[i] for i in range(len(num)-1)]
ans = 1
count1 = 0
for i in range(len(diff)):
    if diff[i] == 3:
        ans *= dp[count1]
        count1 = 0
    else:
        count1 += 1
print("Part 2: ",ans)
