data = open('input.txt','r')
lines = data.readlines()

#lines = ['FBFBBFFRLR','BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
def col_index(line):
    l = 0
    h = 7
    #print("Col Values:" + line)
    for i in range(len(line)-1):
        m = (l+h+1)//2
        if line[i] == 'L':
            h = m-1
        else:
            l = m
        #print(l, m, h)
    if line[len(line)-1]=='L':
        #print("Col index: ", l)
        return l
    else:
        #print("Col index: ", h)
        return h

def row_index(line):
    l = 0
    h = 127
    #print("Row values:"+line)
    for i in range(len(line)-1):
        m = (l + h+1)//2
        if line[i] == 'F':
            h = m-1
        else:
            l = m
        #print(l,m,h)
    if line[len(line)-1]=='F':
        #print("Row index: ", l)
        return l
    else:
        #print("Row index: ", h)
        return h

def pos(line):
    return row_index(line[:7]) * 8 + col_index(line[7:])
seat_num = []
puzzle1_ans = 0
for line in lines:
    a = pos(line)
    puzzle1_ans = max(puzzle1_ans,a)
    seat_num.append(a)

seat_num.sort()

print("Part1: ",puzzle1_ans)
lower = min(seat_num)
higher = max(seat_num)

for i in range(lower+1,higher):
    if not(i in seat_num) and i+1 in seat_num and i-1 in seat_num:
        print("Part2: ",i)


