version = "0.1"
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def draw_board(b):
    """Draws the board"""
    print(u'\u250C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2510')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(b[6], b[7], b[8]))
    print(u'\u251C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2524')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(b[3], b[4], b[5]))
    print(u'\u251C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2524')
    print(u"\u2502 {} \u2502 {} \u2502 {} \u2502".format(b[0], b[1], b[2]))
    print(u'\u2514\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2518')
    

def draw_intro():
    """Prints out game intro and rules"""

    intro = """
TicTacToe v0.1. ©2018 Denis Rasulev.
    
1. Enter number of human players ('1' or '2')
   (1 to play with computer or 2 to play with friend)
2. Select the sign for the Player 1 (X or O).
3. Play by entering number of the cell in your turn:
"""
    print(intro)

    intro_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    draw_board(intro_board)

    start = input("\nShall we start (y/n)? ")
    if start == 'n':
        exit()


def get_number_of_players():
    ok = False
    num_of_players = 0
    while not ok:
        try:
            num_of_players = int(input("How many human players? (1 or 2): "))
        except ValueError:
            print("Please, enter number '1' or '2'!")
        if num_of_players in [1, 2]:
            ok = True
    return num_of_players


def get_player_name(number, name1='', name2=''):
    name1 = input("How shall I call first player? : ")
    if number == 2:
        name2 = input("How shall I call second player? : ")
    return name1, name2


def get_the_sign():
    ok = False
    while not ok:
        the_sign = input("Select sign for the first player (X or O): ")
        if the_sign not in ['x', 'o']:
            print("Please, enter X or O!")
        if the_sign in ['x', 'o']:
            ok = True
    return the_sign


def make_move(cell, sign, board):
    board[cell] = sign
    pass


def end_of_game(b):
    # check horizontals
    if b[0] == b[1] == b[2] == 'x' or b[0] == b[1] == b[2] == 'o':
        return True
    if b[3] == b[4] == b[5] == 'x' or b[3] == b[4] == b[5] == 'o':
        return True
    if b[6] == b[7] == b[8] == 'x' or b[6] == b[7] == b[8] == 'o':
        return True
    # check verticals
    if b[0] == b[3] == b[6] == 'x' or b[0] == b[3] == b[6] == 'o':
        return True
    if b[1] == b[4] == b[7] == 'x' or b[1] == b[4] == b[7] == 'o':
        return True
    if b[2] == b[5] == b[8] == 'x' or b[2] == b[5] == b[8] == 'o':
        return True
    # check diagonals
    if b[0] == b[4] == b[8] == 'x' or b[0] == b[4] == b[8] == 'o':
        return True
    if b[2] == b[4] == b[5] == 'x' or b[2] == b[4] == b[5] == 'o':
        return True
    return False


draw_intro()
# nop = get_number_of_players()
# pl_name1, pl_name2 = get_player_name(nop)
# sign = get_the_sign()

while not end_of_game(board):
    move = int(input("enter cell number to make your move: ")) - 1
    make_move(move, 'x', board)
    draw_board(board)
    end_of_game(board)