def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] or (col - row + i >= 0 and board[i][col - row + i]) or (col + row - i < n and board[i][col + row - i]):
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def place_first_queen_and_solve(n, first_row, first_col):
    board = [[0] * n for _ in range(n)]
    board[first_row][first_col] = 1
    if solve_n_queens(board, first_row + 1, n):
        print("Solution for the n-Queens problem:")
        print_board(board)
    else:
        print("No solution exists for the given placement of the first queen.")

n = int(input("Enter the size of the board (n): "))
first_row = int(input("Enter the row index for the first queen (0-indexed): "))
first_col = int(input("Enter the column index for the first queen (0-indexed): "))

if 0 <= first_row < n and 0 <= first_col < n:
    place_first_queen_and_solve(n, first_row, first_col)
else:
    print("Invalid position for the first queen.")

""" The time complexity is approximately O(N!):
Each recursive call attempts to place a queen in every possible column in the current row and then recursively tries to solve the next row. This branching makes the time complexity grow factorially with N.

We need O(N^2) space to store the board itself since we're using an N×N matrix."""