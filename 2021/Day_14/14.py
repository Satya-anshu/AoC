import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''
def extract_info(lines):
    found_break = False
    insert_between_pair = collections.defaultdict()
    for line in lines:
        if line == '':
            found_break=True
            continue
        if found_break:
            key,value = line.split(" -> ")
            insert_between_pair[key] = value
        else:
            template = line
    return template,insert_between_pair

def create_graph(graph):
    g = collections.defaultdict()
    for k,v in graph.items():
        #kk gives me kv and vk
        k1,k2 = list(k)
        k1v = k1+v
        vk2 = v+k2
        if k not in g:
            g[k] = set()
        g[k].add(k1v)
        g[k].add(vk2)
    return g


def solve(lines,steps):
    template,graph = extract_info(lines)
    g = create_graph(graph)
    # THIS IS A DP PROBLEM!!!
    dp = collections.defaultdict(int)
    for k in graph.keys():
        dp[k] = 0

    for i in range(len(template)-1):
        k = template[i] + template[i+1]
        dp[k] += 1
    
    for step in range(steps):
        # For each step, we add the current values and discard the previous values
        new_dp = {}
        for k in dp.keys():
            new_dp[k] = 0

        for k,v in dp.items():
            for new_k in g[k]:
                new_dp[new_k] += dp[k]
        dp = new_dp
    
    # Now find sum of all the endings.
    commons = collections.defaultdict(int)
    for k,v in dp.items():
        start,end = list(k)
        commons[end]+=v
    
    # Find most and least frequent
    commons = collections.Counter(commons).most_common()
    most_common = commons[0]
    least_common = commons[-1]
    print(most_common[1] - least_common[1])

def solve_1(lines):
    solve(lines,10)

def solve_2(lines):
    solve(lines,40)

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)