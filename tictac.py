import random


def draw_board(board):
    """Draws passed board with pseudo-graphics."""
    print(u'\u250C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2510')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(board[7], board[8], board[9]))
    print(u'\u251C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2524')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(board[4], board[5], board[6]))
    print(u'\u251C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2524')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(board[1], board[2], board[3]))
    print(u'\u2514\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2518')


def get_player_symbol():
    """Allows player to select symbol to play with."""
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input("Select symbol X or O: ").upper()
    return ['X', 'O'] if symbol == 'X' else ['O', 'X']


def who_goes_first():
    """Randomly selects who goes first - player or computer."""
    return 'player' if random.randrange(0, 2) else 'computer'


def play_again():
    """Asks if player wants to play again."""
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')


def make_move(brd, sym, mov):
    """Saves move by writing symbol to the list."""
    brd[mov] = sym
    pass


def end_of_game(b, s):
    """Checks if winning conditions was achieved in game."""
    return True if (b[7] == b[8] == b[9] == s or  # horizontals
                    b[4] == b[5] == b[6] == s or
                    b[1] == b[2] == b[3] == s or
                    b[1] == b[4] == b[7] == s or  # verticals
                    b[2] == b[5] == b[8] == s or
                    b[3] == b[6] == b[9] == s or
                    b[1] == b[5] == b[9] == s or  # diagonals
                    b[3] == b[5] == b[7] == s) else False


def copy_board(board):
    """"Duplicates board for additional manipulations and returns it."""
    duplicate_board = []
    for i in board:
        duplicate_board.append(i)
    return duplicate_board


def is_legal_move(b, m):
    """Checks if move is legal, i.e. if board cell is empty."""
    return b[m] == ' '


def get_player_move(board):
    """Gets input from player where to put symbol and checks if it's allowed."""
    mv = ' '
    while mv not in '123456789' or not is_legal_move(board, int(mv)):
        print('Enter your move (1-9):')
        mv = input()
    return int(mv)


def random_move(board, moves_list):
    """Makes random move."""
    moves = []
    for i in moves_list:
        if is_legal_move(board, i):
            moves.append(i)

    if len(moves) != 0:
        return random.choice(moves)
    else:
        return None


def computer_move(board, computer_symbol):
    """Finds next move for the computer and returns it."""
    if computer_symbol == 'X':
        player_symbol = 'O'
    else:
        player_symbol = 'X'

    # Check if we can win in the next move.
    for i in range(1, 10):
        # Work with copy in order not to alter game's board.
        copy = copy_board(board)
        if is_legal_move(copy, i):
            make_move(copy, computer_symbol, i)
            if end_of_game(copy, computer_symbol):
                return i

    # Check if player could win on their next move and block them.
    for i in range(1, 10):
        copy = copy_board(board)
        if is_legal_move(copy, i):
            make_move(copy, player_symbol, i)
            if end_of_game(copy, player_symbol):
                return i

    # Try to take one of the corners, if they are free.
    move = random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if is_legal_move(board, 5):
        return 5

    # Move on one of the sides.
    return random_move(board, [2, 4, 6, 8])


def is_board_full(board):
    """Returns True if every space on the board has been taken."""
    for i in range(1, 10):
        if is_legal_move(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')
print('Play by entering number')
draw_board(list(range(10)))


while True:
    # Reset the board
    main_board = [' '] * 10
    playerLetter, computerLetter = get_player_symbol()
    turn = who_goes_first()
    print('Randomizing on who goes first...')
    print('The ' + turn + ' will go first.')
    game = True

    while game:
        if turn == 'player':
            # Player’s turn.
            draw_board(main_board)
            p_move = get_player_move(main_board)
            make_move(main_board, playerLetter, p_move)

            if end_of_game(main_board, playerLetter):
                draw_board(main_board)
                print('Hooray! You have won the game!')
                game = False
            else:
                if is_board_full(main_board):
                    draw_board(main_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer’s turn.
            c_move = computer_move(main_board, computerLetter)
            make_move(main_board, computerLetter, c_move)

            if end_of_game(main_board, computerLetter):
                draw_board(main_board)
                print('The computer has beaten you! You lose.')
                game = False

            else:
                if is_board_full(main_board):
                    draw_board(main_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
