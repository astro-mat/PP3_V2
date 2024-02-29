import random
"""
Game variables
"""
scores = {"computer": 0, "player": 0}
board_size = 5
num_ships = 3

"""
LEGEND
@ position of ship
- is a miss
X is a hit
"""

"""
class Board:
    def __init__(self, board_size, num_ships):
        self.board_size = board_size
        self.player_hit = []
        self.player_miss = []
        self.player_ships_found = 0
        self.player_ships = self.random.sample(range(25), 3)
        self.player_attempts = set()
        self.computer_hit = []
        self.computer_miss = []
        self.computer_ships_found = 0
        self.computer_ships = self.random.sample(range(25), 3)

"""
def boards():
    player_ships = random.sample(range(board_size ** 2), num_ships)
    computer_ships = random.sample(range(board_size ** 2), num_ships)
    print("Players ships string is:")
    print(player_ships)         #temp
    print("Computer ships string is:")
    print(computer_ships)       #temp

def get_user_name():
    """
    Function to allow user to input name
    """
    player_name = input("what is your name?: \n")
    print(f"Hello {player_name}") #POSSIBLY TO BE DELETED

def make_guess():
    row = input("Please guess a row (or 'quit' to exit): ")
    column = input("please guess a column (or 'quit' to exit): ")
    coordinate = (int(board_size) * int(row)) + int(column)
    print(f"You guessed {coordinate}") #TO BE DELETED

def new_game():
    """
    Starts a new game. sets the board size and number of ships, resets the scores and initialises the board
    """

    scores["computer"] = 0
    scores["player"] = 0
    print("Welcome to BATTLESHIPS!!")
    print(f"Board Size: {board_size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col 0")
    print("-" * 35)
    get_user_name()
    print("-" * 35)
    boards()
    make_guess()
    
new_game()
