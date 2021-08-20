# function to print the board
def print_board(board):
    line = '----------------------'
    horizontal = '|'
    line_count = 0
    for row in board:
        # variable to print the line
        output = ''
        i = 1
        for element in row:
            if element == 0:
                output += '  '
            else:
                output += str(element) + ' '
            if i == 1:
                output = horizontal + output
            elif i % 3 == 0 :
                output += horizontal
            elif i == 9:
                output += horizontal
            i += 1
        if line_count % 3 == 0:
            print(line)
        line_count += 1
        print(output)
    print(line)

# function to find zero in the board
def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return [i,j]
    return None

# function to check if a value
# can place in a given row and column
def is_valid(board, row, col, value):
    # check if there is a value already exist in row
    if value in board[row]:
        return False
    # check if there is value already exists in column
    for i in board:
        if i[col] == value:
            return False
    # check if the value exists in 3x3 board
    # Given a row and colum
    # identify its position in the board through if statement
    if 0 <= row <= 2:
        if 0 <= col <= 2:
            for i in range(0,3):
                for j in range(0,3):
                    if board[i][j] == value:
                        return False
        elif 3 <= col <= 5:
            for i in range(0,3):
                for j in range(3,6):
                    if board[i][j] == value:
                        return False
        else:
            for i in range(0,3):
                for j in range(6,9):
                    if board[i][j] == value:
                        return False
    if 3 <= row <= 5:
        if 0 <= col <= 2:
            for i in range(3,6):
                    for j in range(0,3):
                        if board[i][j] == value:
                            return False
        elif 3 <= col <= 5:
            for i in range(3,6):
                    for j in range(3,6):
                        if board[i][j] == value:
                            return False
        else:
            for i in range(3,6):
                for j in range(6,9):
                    if board[i][j] == value:
                        return False
    if 6 <= row <= 8:
        if 0 <= col <= 2:
            for i in range(6,9):
                    for j in range(0,3):
                        if board[i][j] == value:
                            return False
        elif 3 <= col <= 5:
            for i in range(6,9):
                    for j in range(3,6):
                        if board[i][j] == value:
                            return False
        else:
            for i in range(6,6):
                for j in range(6,9):
                    if board[i][j] == value:
                        return False
    # Pass all the cases
    return True

# function to solve the sodoku
def solve(board):
    pass

# helper function to solve sudoku
def solve_helper(board):
    # base case
    # return board when the board is filled
    if find_zero(board) is None:
        return board
    check_zero = find_zero(board)
    current_row = check_zero[0]
    current_coulmn = check_zero[1]
    for i in range(1, 10):
        valid = is_valid(board, current_row, current_coulmn, i)
        if valid is True:
            board[current_row][current_coulmn] = i
            result = solve_helper(board)
            if result is not None:
                return result

        board[current_row][current_coulmn] = 0

# Sample maze

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]

#print_board(solve_helper(board))
print_board(board)
#print(find_zero(board))