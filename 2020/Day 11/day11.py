grid = [line.strip('\n') for line in open('in.txt','r').readlines()]

def isSafe(x,y,rows,cols):
    return (0 <= x and x < rows and 0 <= y and y < cols)

def count_adj_seats(grid,row,col, part):
    countF = 0
    for i in range(-1,2):
        for j in range(-1,2):
            x = row
            y = col
            if not (i==0 and j==0):
                while isSafe(x,y,len(grid),len(grid[0])):
                    x += i
                    y += j
                    if isSafe(x,y,len(grid),len(grid[0])):
                        if grid[x][y] == '#':
                            countF += 1
                            break
                        elif grid[x][y] == 'L':
                            break
                        if part == 1:
                            break
    return countF
                        
                    
def rules(grid, countRule, part):
    new_grid = grid.copy()
    new_grid = [list(line) for line in new_grid]
    #print(new_grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            countF = count_adj_seats(grid,i,j, part)
            if countF >= countRule and grid[i][j] == '#':
                new_grid[i][j] = 'L'
            elif countF == 0 and grid[i][j] == 'L':
                new_grid[i][j] = '#'
    return new_grid

def Print(grid):
    for i in grid:
        print(''.join(i))

def Solve(part, countRule, grid):
    prev_grid = grid.copy()
    while True:
        grid = rules(grid, countRule, part)
        if grid == prev_grid:
            break
        else:
            prev_grid = grid.copy()

    occ = 0
    for i in grid:
        occ += i.count('#')
    print("Part {0}: {1}".format(part,occ))

temp = grid.copy()
Solve(1,4, temp)
Solve(2,5, grid)
