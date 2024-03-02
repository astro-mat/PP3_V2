import random

"""
Game variables
"""
scores = {"computer": 0, "player": 0}
board_size = 5
num_ships = 3
num_turns = 5

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

def display_player_board():
    print("\n    0  1  2  3  4")
    for row in range(5):
        line = ""
        for column in range(board_size):
            place = 5 * row + column
            if place in computer_hit:
                ch = " X "
            elif place in computer_miss:
                ch = " O "
            elif place in player_ships:
                ch = " @ "
            else:
                ch = " · "
            line += ch
            place += 1
        print(row, "", line)


def display_computer_board():
    print("\n    0  1  2  3  4")
    for row in range(5):
        line = ""
        for column in range(board_size):
            place = 5 * row + column
            if place in player_hit:
                ch = " X "
            elif place in player_miss:
                ch = " O "
            else:
                ch = " · "
            line += ch
            place += 1
        print(row, "", line)


def computer_guess():
    return random.randint(0, 24)


def end_game():
    play_again = str(input("Do you want to play again? (type Y to play again or anything else to continue playing): "))
    if play_again.upper() == "Y":
        play_game()
    else:
        print("Thankyou for playing. Goodbye!")
        return



def play_game():
    num_turns_taken = 0
    while num_turns_taken < 5:
        print("Players ships string is:")
        print(player_ships)         #temp
        print("Players hits string is:")
        print(player_hit)         #temp
        print("Players misses string is:")
        print(player_miss)         #temp
        print(f"{player_name}'s Board")
        display_player_board()

        print("Computer ships string is:")
        print(computer_ships)       #temp
        print("Computer hits string is:")
        print(computer_hit)       #temp
        print("Computer misses string is:")
        print(computer_miss)       #temp
        print("Computers Board")
        display_computer_board()
    
        print("-" * 35)
        print(f"You have used {num_turns_taken} out of {num_turns} turns")
        print(f"You have {5 - num_turns_taken} turns left")
        row = input("Please guess a row (or type 'Q' to quit/exit): ")
        if row.upper() == "Q":
            return end_game()
        column = input("please guess a column (or 'quit' to exit): ")
        print("-" * 35)
        if row.upper() == "Q":
            return end_game()
        coordinate = (int(board_size) * int(row)) + int(column)
        print(f"You guessed {coordinate}") #TO BE DELETED
        num_turns_taken = num_turns_taken + 1
        """
        Check if the guess is in computer_ships
        """
        try:
            if coordinate in computer_ships:
                computer_ships.remove(coordinate)
                player_hit.append(coordinate)
                print("You hit a ship")
                print("Computer ships string is now:")
                print(computer_ships)
                print("-" * 35)
            else:
                computer_miss.append(coordinate)
                player_hit.append(coordinate)
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
            computer_hit.append(computer_coordinate)
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
        print(f"You have ran out of turns {player_name}. Game over!")
        end_game()


scores["computer"] = 0
scores["player"] = 0

print("Welcome to BATTLESHIPS!!")

print("-" * 35)
player_name = input("Please enter your name: \n")
print("-" * 35)
"""
# level of difficulty
print(f"Please choose your prefered level of difficulty {player_name}")
difficulty = input("easy (1), Medium (2) or Hard (3)")
print("-" * 35)
if difficulty == 1:
    board_size = 5
    num_ships = 5
    num_turns = 10
elif difficulty == 2:
    board_size = 5
    num_ships = 3
    num_turns = 5
elif difficulty == 3:
    board_size = 5
    num_ships = 2
    num_turns = 3

print(f"You have selected difficulty of {difficulty}")
"""
print(f"The Board Size is {board_size}.")
print(f"The number of ships is {num_ships}.")
print(f"You will have {num_turns} turns.")
print("Top left corner is row: 0, col 0")

computer_board = Board(board_size, num_ships, "Computer", type="computer")    # class instance for computer_board
player_board = Board(board_size, num_ships, player_name, type="player")       # Class instance for player board


computer_ships = computer_board.create_boards()
computer_hit = []
computer_miss = []
 
player_ships = player_board.create_boards()
player_hit = []
player_miss = []



play_game()

