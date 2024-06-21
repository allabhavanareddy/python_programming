def issafe(board, r, c):
    # Check the column
    for i in range(r):
        if board[i][c] == '1':
            return False

    # Check the diagonal from top-left to bottom-right
    i, j = r - 1, c - 1
    while i >= 0 and j >= 0:
        if board[i][j] == '1':
            return False
        i -= 1
        j -= 1

    # Check the diagonal from top-right to bottom-left
    i, j = r - 1, c + 1
    while i >= 0 and j < len(board):
        if board[i][j] == '1':
            return False
        i -= 1
        j += 1

    return True

def queen(board, r, count):
    if r == len(board):
        return True
    
    for c in range(len(board)):
        if issafe(board, r, c):
            board[r][c] = '1'
            count[0] += 1
            if queen(board, r + 1, count):
                return True
            board[r][c] = '0'
            count[0] -= 1
    return False

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def queens(n):
    board = [['0' for _ in range(n)] for _ in range(n)]
    count = [0]  # Use a list to keep track of the number of queens placed
    if queen(board, 0, count):
        print_board(board)
        print(count[0])
    else:
        print("No solution")

n = int(input())
queens(n)
