from collections import Counter

def solve(s):
    ans1 = ans2 = 0
    for line in s.splitlines():
        nums, char, pwd = line.split()
        pwd_count = Counter(pwd)
        char = char[0]
        l,_,r = nums.partition("-")
        if int(l) <= pwd_count[char] <= int(r):
            ans1 += 1
        ans2 += (pwd[(int(l)-1)] == char) ^ (pwd[int(r)-1] == char)
    return ans1, ans2

s = open('in.txt','r').read()
ans1, ans2 = solve(s)
print("Part 1: ", ans1)
print("Part 2: ", ans2)
