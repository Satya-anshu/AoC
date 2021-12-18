import os
import copy
import collections
from itertools import permutations

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

test_input = \
'''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
'''

test_input_larger = \
'''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
'''

test_input_2 = \
'''[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]
'''

test_input_3 = \
'''[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
'''

test_input_4 = \
'''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
'''
def reduce_expr(expr):
    l = list(expr)
    while True:
        a = []
        for i in range(len(l)):
            if l[i] == '[':
                a.append(i)
            elif l[i] == ']':
                a.pop()
            # Found a pair to explode
            if len(a) == 5 and l[i+4] == ']':
                break
        
        # Find 2 digit numbers in the list
        for k in range(len(l)):
            if len(l[k]) > 1:
                break
        
        # Always explode first!
        if i != len(l) - 1:
            # Get the 2 numbers
            nums = [int(n) for n in (l[i+1],l[i+3])]

            # Check right
            for w in range(i+5,len(l)):
                if l[w].isdigit():
                    break
            if w != len(l) -1:
                l[w] = str(int(l[w]) + nums[1])
            
            # Check left
            for q in range(i-1,-1,-1):
                if l[q].isdigit():
                    break
            if q != 0:
                l[q] = str(int(l[q]) + nums[0])

            # Create new list after explosion
            l = l[:i] + ['0'] + l[i+5:]
        
        # If can't explode, try to split the number
        elif k != len(l) - 1:
            # Split the number into 2
            l = l[:k] + ["[", str(int(l[k])//2), ",", str((int(l[k])+1)//2),"]"] + l[k+1:]
        
        # Else, Done!
        else:
            break

    return ''.join(l)

def get_sum(reduced_expr):
    while len(reduced_expr) > 1:
        p = []
        for i in range(len(reduced_expr)):
            if reduced_expr[i] == '[':
                p.append(i)
            if reduced_expr[i] == ']':
                break
        nums = [int(n) for n in (reduced_expr[p[-1]+1],reduced_expr[p[-1]+3])]
        n = nums[0] *3 + nums[1] * 2
        reduced_expr = reduced_expr[:p[-1]] + [str(n)] + reduced_expr[p[-1]+5:]
    
    return int(reduced_expr[0])

def solve_1(expressions):
    reduced_expr = expressions[0]
    for i in range(1,len(expressions)):
        # Do addition first
        add = '[' + reduced_expr + ',' + expressions[i] + ']'
        reduced_expr = reduce_expr(add)
    
    reduced_expr = list(reduced_expr)
    print(get_sum(reduced_expr))


def solve_2(expressions):
    max_sum = -1

    # Neat permutation trick from itertools
    for p in permutations(expressions,2):
        add = "[" + p[0] + "," + p[1] + "]"
        reduced_expr = reduce_expr(add)
        reduced_expr = list(reduced_expr)
        max_sum = max(max_sum,get_sum(reduced_expr))
    print(max_sum)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input_larger.splitlines()
    solve_1(lines)
    solve_2(lines)