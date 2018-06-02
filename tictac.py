import random


def draw_board(board):
    """Draws passed board with pseudo-graphics"""
    print(u'\u250C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2510')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(board[7], board[8], board[9]))
    print(u'\u251C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2524')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(board[4], board[5], board[6]))
    print(u'\u251C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2524')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(board[1], board[2], board[3]))
    print(u'\u2514\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2518')


def get_player_symbol():
    symbol = ''
    while symbol not in 'XO':
        symbol = input("Select symbol X or O: ").upper()
    return ['X', 'O'] if symbol == 'X' else ['O', 'X']


def who_goes_first():
    return 'player' if random.randrange(0, 2) else 'computer'


def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')


def make_move(board, symbol, move):
    board[move] = symbol
    pass


def end_of_game(b, s):
    return True if (b[7] == b[8] == b[9] == s or  # horizontals
                    b[4] == b[5] == b[6] == s or
                    b[1] == b[2] == b[3] == s or
                    b[1] == b[4] == b[7] == s or  # verticals
                    b[2] == b[5] == b[8] == s or
                    b[3] == b[6] == b[9] == s or
                    b[1] == b[5] == b[9] == s or  # diagonals
                    b[3] == b[5] == b[7] == s) else False


def is_legal_move(b, m):
    return b[m] == ' '


def get_player_move(board):
    move = ' '
    while move not in '123456789' or not is_legal_move(board, int(move)):
        print('Enter your move (1-9):')
        move = input()
    return int(move)


