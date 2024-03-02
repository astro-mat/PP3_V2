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
    
def computer_guess():
    return random.randint(0, 24)


def play_game():
    num_turns = 0
    while num_turns < 5:
        print("-" * 35)
        print(f"You have used {num_turns} out of 5 turns")
        print(f"You have {5 - num_turns} turns left")
        row = input("Please guess a row (or 'quit' to exit): ")
        column = input("please guess a column (or 'quit' to exit): ")
        coordinate = (int(board_size) * int(row)) + int(column)
        print(f"You guessed {coordinate}") #TO BE DELETED
        num_turns = num_turns + 1
        """
        Check if the guess is in computer_ships
        """
        try:
            if coordinate in computer_ships:
                computer_ships.remove(coordinate)
                print("You hit a ship")
                print("Computer ships string is now:")
                print(computer_ships)
                print("-" * 35)
            else:
                print("you missed, try again")
                print("-" * 35)
            
        except ValueError:
            print("Incorrect coordinates.")
            print("Please enter your guess as a number.\n")
        
        """
        computer turn
        """
        computer_coordinate = computer_guess()

        if computer_coordinate in player_ships:
            player_ships.remove(computer_coordinate)
            print(f"computer guessed {computer_coordinate} and hit one of your ships")
            print("player ships string is now:")
            print(player_ships)
            print("computer ships string is:")
            print(computer_ships)
        else:
            print(f"computer guessed {computer_coordinate} and missed your ship")
            print("player ships string is:")
            print(player_ships)
            print("computer ships string is:")
            print(computer_ships)
    else:
        print("You have ran out of turns. Game over!")


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
print(player_ships)         #temp
print("Computer ships string is:")
print(computer_ships)       #temp
play_game()

