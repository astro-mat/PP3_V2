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
class Board:
    def __init__(self):
        self.player_ships = []

        self.computer_ships = []


    def create_board():
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
    """
    Check if the guess is in computer_ships
    """
    """
    if coordinate in create_board.computer_ships:
        create_board.computer_ships.pop(coordinate)
        print("You hit a ship")
        print("Computer ships string is now:")
        print(create_board.computer_ships)
    else:
        print("you missed, try again")
    """

    """
    Starts a new game. sets the board size and number of ships, resets the scores and initialises the board
    """

scores["computer"] = 0
scores["player"] = 0
print("Welcome to BATTLESHIPS!!")
print(f"Board Size: {board_size}. Number of ships: {num_ships}")
print(" Top left corner is row: 0, col 0")
print("-" * 35)
Board.get_user_name()
print("-" * 35)
Board.create_board()
make_guess()
    

