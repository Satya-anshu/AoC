import collections
lines = open('in.txt','r').read()

def cycle_cubes(s):
    space = {}
    for y,line in enumerate(s.splitlines()):
        for x,c in enumerate(line):
            if c=='#':
                space[(x,y,0)] = c

    for _ in range(6):
        marked = collections.Counter()

        for (x,y,z), c in space.items():
            for x_i in (-1,0,1):
                for y_i in (-1,0,1):
                    for z_i in (-1,0,1):
                        if x_i == y_i == z_i ==  0:
                            continue
                        marked[(x+x_i,y+y_i,z+z_i)] += 1

        new_space = {}
        for k,v in marked.items():
            if v==3:
                new_space[k] = '#'

        for k in space:
            if marked[k] in {2,3}:
                new_space[k] = '#'

        space = new_space
        
    return len(space)

print("Part 1: ", cycle_cubes(lines))
    
