num = (''.join(open('in.txt','r').readlines()).strip('\n'))
l = [num[i:i+150] for i in range(0,len(num),150)]

part1 = 10 ** 10
layer1 = 0
ctr = 0
for i in l:
    if part1 > i.count('0') and i != '':
        layer1 = ctr
        part1 = i.count('0')
    ctr += 1
print("Part 1: ", l[layer1].count('1') * l[layer1].count('2'))

ans = ['2' for i in range(150)]
for i in range(0,150):
    for j in range(len(l)):
        if l[j][i] == '0' or l[j][i]== '1':
            ans[i] = l[j][i]
            break
ctr = 0
ans = [ans[i:i+25] for i in range(0,150,25)]
print("Part 2: ")
for i in ans:
    for j in i:
        if j == '0':
            print(' ',end='')
        elif j== '1':
            print('#',end='')
        else:
            print('O',end='')
    print('')
