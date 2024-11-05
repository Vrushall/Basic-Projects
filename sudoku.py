sudoku_list = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

#making the sudoku look like a sudoku
def print_sudoku(list):
    
    for row in list:
        print(" ".join(str(num) if num != 0 else "." for num in row)) #just goes through the rows in the list and making the numbers in strings and makes the zeroes into dots

print_sudoku(sudoku_list)

#finding the empty cells until there are none left
def find_empty(board):
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  #row, col
    return None  

#checking if the number can go in the row,col and grid
def is_valid(board, row, col, num):
    #row
    for j in range(9):
        if board[row][j] == num:
            return False

    #column
    for i in range(9):
        if board[i][col] == num:
            return False

    #grid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

#solving using backtracking
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # No empty cells left
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Try placing num

            if solve(board):  # Recursively solve the rest of the board
                return True

            board[row][col] = 0  # Reset if no solution found with num

    return False

if solve(sudoku_list):
    print("Solved=")
    print_sudoku(sudoku_list)
else:
    print("Soluton does not exist") #just in case