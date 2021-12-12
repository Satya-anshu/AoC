import os
import copy
import collections

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''

test_input_small = \
'''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

def get_graph(lines):
    graph = collections.defaultdict(list)
    for line in lines:
        u,v = line.split("-")
        graph[u].append(v)
        graph[v].append(u)
    return graph

def count_paths(g, node, vis = set(), again = False):
    if node == 'end':
        return 1
    
    new_vis = vis | {node} if node.islower() else vis
    count = 0
    for to in g[node]:
        if to == 'start': continue
        if to in vis:
            if again: continue
            else:
                count += count_paths(g,to,new_vis,True)
        else:
            count += count_paths(g,to,new_vis,again)
    return count

def solve_1(lines):
    print(count_paths(get_graph(lines),'start',again=True))

def solve_2(lines):
    print(count_paths(get_graph(lines),'start',again=False))

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input_small.splitlines()
    solve_1(lines)
    solve_2(lines)