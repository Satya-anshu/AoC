import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''
def solve_1(lines):
    cnt_unique = 0
    for line in lines:
        outputs = line.split("|")[1].split()
        for output in outputs:
            if len(output) in (2,3,4,7):
                cnt_unique+=1
    print(cnt_unique)

def process_inputs(inputs):
    '''
    000
    1 2
    333
    4 5
    666
    Number 2 is same as Number 5 is same as Number 3 => Segment_length = 5
    Number 6 is same as Number 9 is same as Number 0 => Segment_length = 6
    Number 1, 4, 7, 8 have unique segment lengths
    '''
    dict = {}
    for inp in inputs:
        set_inp = set(inp)
        if len(inp) == 4:
            dict[4] = set_inp
        elif len(inp) == 2:
            dict[1] = set_inp
        elif len(inp) == 3:
            dict[7] = set_inp
        elif len(inp) == 7:
            dict[8] = set_inp
    
    for inp in inputs:
        set_inp = set(inp)
        if len(inp) == 5:
            if len(set_inp.intersection(dict[1])) == 2:
                dict[3] = set_inp
            elif len(set_inp.intersection(dict[4])) == 2:
                dict[2] = set_inp
            else:
                dict[5] = set_inp
        elif len(inp) == 6:
            if len(set_inp.intersection(dict[4])) == 4:
                dict[9] = set_inp
            elif len(set_inp.intersection(dict[1])) == 1:
                dict[6] = set_inp
            else:
                dict[0] = set_inp
    return dict

def process_mapping(mapping, outputs):
    num = ''
    for output in outputs:
        for k,v in mapping.items():
            if set(v) == set(output):
                num+=str(k)
    return int(num)

def solve_2(lines):
    total = 0
    for line in lines:
        inputs,outputs = line.split("|")
        inputs = inputs.split()
        outputs = outputs.split()
        mapping = process_inputs(inputs)
        total += process_mapping(mapping,outputs)
    print(total)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)