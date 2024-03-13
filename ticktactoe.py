# define print board to terminal every move
def print_board(board):
    print("-" * 9)
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# test print_board with 3x3 empty board
# print(print_board([[' ' for _ in range(3)] for _ in range(3)]))

# define check winner every move
def check_winner(board):
    # check row
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # check column
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != ' ':
        return board[2][0]
    return ''

def tick_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = input('Chose first player (x / o): ').upper()
    move_count = 0
    winner = ''
    print_board(board)
    
    current_move = 'invalid'

    while winner =='':
        print(f'Current player {current_player} turn:')
        while current_move == 'invalid':
            try:
                row = int(input('Pick row (0, 1, 2): '))
                col = int(input('Pick column (0, 1, 2): '))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print('Input is out of range. Retry other')
                elif board[row][col] != ' ':
                    print('Position is taken. Retry other')
                    continue
                else:
                    move_count += 1
                    print('****************')
                    print(f'{move_count} moved: {current_player} row {row}, column {col}')
                    current_move = 'valid'
            except ValueError:
                print('Please input a Number')
        board[row][col] = current_player
        print_board(board)
        print('****************')

        # check winner
        winner = check_winner(board)
        if winner != '':
            print(f'Player {current_player} won, congratulation!')
            break
   
        # check if Tie
        if move_count >= 9:
            print('It\' a tie!')
            break
        # reset conditions
        current_move = 'invalid'
        if current_player == 'X':
            current_player = "O"
        else:
            current_player = 'X'


tick_tac_toe()

