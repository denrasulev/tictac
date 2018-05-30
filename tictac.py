version = "0.1"
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


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

    print("\nTicTacToe v{}. ©2018 Denis Rasulev.".format(version))
    print("---")
    print("Rules:")


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


def get_player_name(player=""):
    name = input(f"How shall I call {player}? : ")
    return name


draw_intro()
draw_board(board)
nop = get_number_of_players()
print(nop)
pl1_name = get_player_name("Player 1")
print(pl1_name)