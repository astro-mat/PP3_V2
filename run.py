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
    def __init__(self, board_size, num_ships, player_name, type):
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_name = player_name
        self.type = type



    def create_user(self):
        """
        instance method to
        Store user name
        Keep Score
        """
        pass

    def create_boards(self):
        """
        instance method to create the boards
        """
        return random.sample(range(self.board_size ** 2), self.num_ships)



"""
def make_guess():
    row = input("Please guess a row (or 'quit' to exit): ")
    column = input("please guess a column (or 'quit' to exit): ")
    coordinate = (int(board_size) * int(row)) + int(column)
    print(f"You guessed {coordinate}") #TO BE DELETED
"""
    
def play_game():
    row = input("Please guess a row (or 'quit' to exit): ")
    column = input("please guess a column (or 'quit' to exit): ")
    coordinate = (int(board_size) * int(row)) + int(column)
    print(f"You guessed {coordinate}") #TO BE DELETED
    """
    Check if the guess is in computer_ships
    """
    if coordinate in computer_ships:
        computer_ships.remove(coordinate)
        print("You hit a ship")
        print("Computer ships string is now:")
        print(computer_ships)
    else:
        print("you missed, try again")







scores["computer"] = 0
scores["player"] = 0
print("Welcome to BATTLESHIPS!!")
print(f"Board Size: {board_size}. Number of ships: {num_ships}")
print(" Top left corner is row: 0, col 0")
print("-" * 35)
player_name = input("Please enter your name: \n")
print("-" * 35)

computer_board = Board(board_size, num_ships, "Computer", type="computer")    # class instance for computer_board
player_board = Board(board_size, num_ships, player_name, type="player")       # Class instance for player board


computer_ships = computer_board.create_boards()
player_ships = player_board.create_boards()

print("Players ships string is:")
print(computer_ships)         #temp
print("Computer ships string is:")
print(player_ships)       #temp
play_game()

