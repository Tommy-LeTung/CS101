# define print board to terminal every move
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# test print_board with 3x3 empty board
# print(print_board([[' ' for _ in range(3)] for _ in range(3)]))

# define check winner every move
def check_winner(board):
    # check row
    for row in board:
        if row[0] == row[1] == row[2] == ' ':
            return row[0]
    # check column
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] == ' ':
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == ' ':
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] == ' ':
        return board[2][0]
    return None



