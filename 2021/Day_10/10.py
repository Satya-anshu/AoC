import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
def solve_1(lines):
    error_score = 0
    for line in lines:
        stk = []
        for bkt in line:
            if bkt in ('(','[','{','<'):
                stk.append(bkt)
            else:
                if stk[-1] == '(' and bkt != ')' or stk[-1] == '{' and bkt != '}' or stk[-1] == '[' and bkt != ']' or stk[-1] == '<' and bkt != '>':
                    if bkt == ')':
                       error_score+=3
                    elif bkt == ']':
                        error_score+=57
                    elif bkt == '}':
                        error_score+=1197
                    else:
                        error_score+=25137
                    break
                else:
                    stk.pop(-1)
    print(error_score)

def solve_2(lines):
    incomplete_scores = []
    for line in lines:
        stk = []
        error = False
        for bkt in line:
            if bkt in ('(','[','{','<'):
                stk.append(bkt)
            else:
                if stk[-1] == '(' and bkt != ')' or stk[-1] == '{' and bkt != '}' or stk[-1] == '[' and bkt != ']' or stk[-1] == '<' and bkt != '>':
                    error = True
                    break
                else:
                    stk.pop(-1)
        if error:
            continue
        score = 0
        for rem_bkt in reversed(stk):
            if rem_bkt == '(':
                val = 1
            elif rem_bkt == '[':
                val = 2
            elif rem_bkt == '{':
                val = 3
            else:
                val = 4
            score = score * 5 + val
        incomplete_scores.append(score)
    incomplete_scores.sort()
    print(incomplete_scores[len(incomplete_scores)//2])

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)