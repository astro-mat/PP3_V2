import random
"""
Game variables
"""

scores = {"computer": 0, "player": 0}

"""
LEGEND
@ position of ship
- is a miss
X is a hit
"""


def get_user_name():
    player_name = input("what is your name?: \n")
    print(f"the data provided is {player_name}")

def make_guess():
    row = input("Please guess a row (or 'quit' to exit): ")
    column = input("please guess a column (or 'quit' to exit): ")
    coordinates = [row, column]
    print(coordinates)



def new_game():
    """
    Starts a new game. sets the board size and number of ships, resets the scores and initialises the board
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("Welcome to BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col 0")
    print("-" * 35)
    get_user_name()
    print("-" * 35)
    make_guess()

new_game()
