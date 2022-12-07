import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

class Node:
    def __init__(self):
        self.data = {}
        self.next = None
        self.prev = None


def parse(lines):
    root = Node()
    curr = root
    head = root
    cmd = ""
    for line in lines:
        if '$' in line: # '$' is a command
            cmd = line.split(" ")
            if cmd[1] == 'cd':
                # Change directory.
                loc = cmd[2]
                if loc == '/':
                    head = root
                    curr = root
                elif loc == '..':
                    # go up one directory
                    curr = curr.prev
                else:
                    if loc in curr.data:
                        curr = curr.data[loc]
            else:
                # command is ls [list files]
                continue
        else:
            ls_output = line.split(" ")
            if 'dir' == ls_output[0]:
                loc = ls_output[1]
                if loc not in curr.data:
                    new_node = Node()
                    new_node.prev = curr
                    curr.data.update({loc: new_node})
                    
            else:
                sz = int(ls_output[0])
                file_name = ls_output[1]
                curr.data.update({file_name: sz})
    return head                   


directories_less_than_1l = []
directories_sizes = []
def get_size(dir):
    sz = 0
    for v in dir.data.values():
        if type(v) is Node:
            directories_sizes.append(get_size(v))
            sz += directories_sizes[-1]
        else:
            sz += v
    if sz < 100000:
        directories_less_than_1l.append(sz)
    return sz


def solve_1():
    return sum(directories_less_than_1l)


def solve_2():
    unused_size = 70000000 - total_size
    required_free_size = 30000000 - unused_size
    directories_sizes.sort()
    for d in directories_sizes:
        if d >= required_free_size:
            return d
    
if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    dir = parse(lines)
    total_size = get_size(dir)
    print('Part 1: ',solve_1())
    print('Part 2: ',solve_2())