DIRS = [
    (1,1),
    (5,1),
    (7,1),
    (1,2),
    ]

def solve(s, dx, dy):
    x = y = 0
    count = 0
    grid = s.splitlines()
    while y < len(grid):
        if grid[y][x] == '#':
            count += 1
        y += dy
        x += dx
        if x >= len(grid[0]):
            x -= len(grid[0])
    return count
            
            
s = open('in.txt','r').read()

ans = solve(s, 3, 1)
print("Part 1: ", ans)

for right, down in DIRS:
    ans *= solve(s, right, down)
print("Part 2: ", ans)
