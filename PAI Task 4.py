def is_safe(board, row, col, n):

    
    for i in range(col):
        if board[row][i] == 1:
            return False

 
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

  
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):

    
    if col >= n:
        return True

    for i in range(n):

        if is_safe(board, i, col, n):

            board[i][col] = 1

            if solve_n_queens(board, col + 1, n):
                return True

            
            board[i][col] = 0

    return False


def print_board(board, n):

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()



n = int(input("Enter number of queens: "))

board = [[0 for _ in range(n)] for _ in range(n)]

if solve_n_queens(board, 0, n):
    print("\nSolution for", n, "Queens:\n")
    print_board(board, n)
else:
    print("No solution exists.")