import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


test_input = \
'''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

def check(board):
    for i in range(len(board)):
        if(sum(board[i]) == -1 * len(board[i])):
            return True
    row_sum = 0
    col_sum = [0 for j in range(len(board[i]))]
    for i in range(len(board)):
        row_sum = 0
        for j in range(len(board[i])):
            row_sum += board[i][j]
            col_sum[j] += board[i][j]

        if(row_sum == -1*len(board[i])):
            return True
        for j in col_sum:
            if j == -1*len(board[i]):
                return True
    return False

def extract_info(lines):
    # Extract bingo numbers and boards
    bingo_nums = list(map(int,lines[0].split(',')))
    boards = []
    matrix = []
    for i in range(2,len(lines)):
        if lines[i] == '':
            boards.append(matrix)
            matrix = []
        else:
            matrix.append(list(map(int,lines[i].split())))
    boards.append(matrix)
    return bingo_nums, boards

def solve_1(lines):
    # Simulation problem
    bingo_nums,boards = extract_info(lines)

    # For each bingo num, mark the board and check if it wins or not (row & col)
    for num in bingo_nums:
        for board in boards:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(board[i][j] == num):
                        board[i][j] = -1
            
            if(check(board)):
                #print("Board number: ",board)
                #print("Bingo num: ", num)
                ans = 0
                for row in board:
                    for val in row:
                        if val != -1:
                            ans += val
                print(ans * num)
                return

def solve_2(lines):
    bingo_nums,boards = extract_info(lines)
    boards_not_won = set()
    for i in range(len(boards)):
        boards_not_won.add(i)
    
    # For each bingo num, mark the board and check if it wins or not (row & col)
    for num in bingo_nums:
        for board_num,board in enumerate(boards):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(board[i][j] == num):
                        board[i][j] = -1
            
            if(board_num in boards_not_won and check(board)):
                boards_not_won.remove(board_num)
                
                if len(boards_not_won) != 0:
                    continue
                ans = 0
                for row in board:
                    for val in row:
                        if val != -1:
                            ans += val
                print(ans * num)
                return

if __name__ == "__main__":
    lines = open("input.txt","r").read().splitlines()
    linesTest = test_input.splitlines()
    solve_1(lines)
    solve_2(lines)