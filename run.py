import random

# Game variables


board_size = 5
num_ships = 3
num_turns = 5


class Board:
    def __init__(self, board_size, num_ships, player_name, type):
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_name = player_name
        self.type = type

    def create_user(self):

        # instance method to Store user name Keep Score

        pass

    def create_boards(self):

        # instance method to create the boards

        return random.sample(range(self.board_size ** 2), self.num_ships)

class Game:
    pass

class User:
    pass

def display_player_board():
    print("\n    0  1  2  3  4")
    print("    _  _  _  _  _")
    for row in range(5):
        line = ""
        for column in range(board_size):
            place = 5 * row + column
            if place in computer_hit:
                character = "|X|"
            elif place in computer_miss:
                character = "|O|"
            elif place in player_ships:
                character = "|@|"
            else:
                character = "|_|"
            line += character
            place += 1
        print(row, "", line)


def display_computer_board():
    print("\n    0  1  2  3  4")
    print("    _  _  _  _  _")
    for row in range(5):
        line = ""
        for column in range(board_size):
            place = 5 * row + column
            if place in player_hit:
                character = "|X|"
            elif place in player_miss:
                character = "|O|"
            else:
                character = "|_|"
            line += character
            place += 1
        print(row, "", line)


def computer_guess():
    return random.randint(0, 24)


def end_game():
    print("Do you want to play again?")
    print("(type Y to play again")
    play_again = str(input(" or any other key to quit):\n"))
    if play_again.upper() == "Y":
        play_game()
    else:
        print("Thankyou for playing. Goodbye!")
        return


def play_game():
    num_turns_taken = 0
    while num_turns_taken < 5:
        print(f"{player_name}'s Board")
        display_player_board()
        print("Players ships string is:")   #temp
        print(player_ships)                 #temp
        print("Players hits string is:")    #temp
        print(player_hit)                   #temp
        print("Players misses string is:")  #temp
        print(player_miss)                  #temp
        print("\nComputers Board")
        display_computer_board()
        print("Computer ships string is:")  #temp
        print(computer_ships)               #temp
        print("Computer hits string is:")   #temp
        print(computer_hit)                 #temp
        print("Computer misses string is:") #temp
        print(computer_miss)                #temp
        print("-" * 35)
        print(f"You have used {num_turns_taken} out of {num_turns} turns")
        print(f"You have {5 - num_turns_taken} turns left")

        # row = input("Please guess a row (or type 'Q' to quit/exit): \n")
        row = validate_coordinate("Please guess a row (or type 'Q' to quit/exit): \n", ['0', '1', '2', '3', '4', 'Q'])
        if row.upper() == "Q":
            return end_game()
        # column = input("please guess a column (or 'quit' to exit): \n")
        column = validate_coordinate("Please guess a column (or 'quit' to exit): \n", ['0', '1', '2', '3', '4', 'Q'])
        if column.upper() == "Q":
            return end_game()
        print("-" * 35)
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
                print("-" * 35)
            else:
                computer_miss.append(coordinate)
                player_hit.append(coordinate)
                print("you missed, try again")
                print("-" * 35)
        except ValueError:
            print("Incorrect coordinates.")
            print("Please enter your guess as a number.\n")

        # computer turn

        computer_coordinate = computer_guess()

        if computer_coordinate in player_ships:
            player_ships.remove(computer_coordinate)
            computer_hit.append(computer_coordinate)
            print(f"computer guessed {computer_coordinate}\n")
            print("and hit one of your ships!")
        else:
            print(f"computer guessed {computer_coordinate}\n")
            print("and missed your ships\n")

    else:
        print(f"You have ran out of turns {player_name}. Game over!")
        end_game()


def get_user_name():
    input_is_valid = False
    while input_is_valid is False:
        user_input = input("Please enter your name (3 letters or more): \n")
        if user_input:
            if len(user_input) >= 3:
                input_is_valid = True
            else:
                print('Name should be 3 letters or more')
        else:
            print('Cant have an empty Name')
    return user_input

def validate_coordinate(input_message, valid_values):
    input_is_valid = False
    while input_is_valid is False:
        user_input = input(input_message)
        if user_input:
            if user_input.upper() in valid_values:
                input_is_valid = True
            else:
                print(f'Please enter one of the following values {valid_values}')
        else:
            print('Coordinate cant be empty')
    return user_input


print("Welcome to BATTLESHIPS!!")

print("-" * 35)
player_name =  get_user_name()
print("-" * 35)
print(f"The Board Size is {board_size}.")
print(f"The number of ships is {num_ships}.")
print(f"You will have {num_turns} turns.")
print("Top left corner is row: 0, col 0\n")
print("--LEGEND--")
print("@ Is a ship")
print("- Is a miss")
print("X Is a hit")
print("-" * 35)

# class instance for computer_board
computer_board = Board(board_size, num_ships, "Computer", type="computer")
# Class instance for player board
player_board = Board(board_size, num_ships, player_name, type="player")

computer_ships = computer_board.create_boards()
computer_hit = []
computer_miss = []

player_ships = player_board.create_boards()
player_hit = []
player_miss = []

play_game()