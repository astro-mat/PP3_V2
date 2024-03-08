import random


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

# BOARD CLASS-------------------------------------------------------------------------------------
class Board:
    
    def __init__(self, board_type, board_size=5, num_ships=3):
        self.board_size = board_size
        self.num_ships = num_ships
        self.board_type = board_type
        self.misses = []
        self.hits = []
        self.ships = random.sample(range(self.board_size ** 2), self.num_ships)


    def display(self, misses=[], hits=[], hidden=True):
        print(f"{self.board_type}'s Board:")
        coordinates = ''
        dash_coordinates = ''
        for coordinate in range(self.board_size):
            coordinates += str(coordinate) + '  '
            dash_coordinates += '_  '
        print(f"\n    {coordinates}")
        print(f"    {dash_coordinates}")
        for row in range(self.board_size):
            line = ""
            for column in range(self.board_size):
                place = self.board_size * row + column
                if place in hits:
                    character = "|X|"
                elif place in misses:
                    character = "|O|"
                elif place in self.ships:
                    if hidden:
                        character = "|_|"
                    else:
                        character = "|@|"
                else:
                    character = "|_|"
                line += character
                place += 1
            print(row, "", line)
        print("\n")

# Checks that the coordinate entered is valid

    def validate_coordinate(self, input_message, valid_values):
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
    
# GAME CLASS---------------------------------------------------------------------------------------------------

class Game:

    def __init__(self, board_size=5, num_ships=3, num_turns=10):
        self.board_size = board_size
        self.num_ships = num_ships
        self.num_turns = num_turns
        self.num_turns_taken = 0
        print("Welcome to BATTLESHIPS!!\n")
        print("Play against the computer to see who wins!")
        print("choose where to fire on the grid and see")
        print("if you hit one of the computers ships")
        print("Then wait to see if the computer hits one of yours!")
        print("First to sink all their opponents ships wins")
        print("-" * 35)
        self.player_name = get_user_name()
        print(f"Thanks for playing {self.player_name}")
        print(f"The Board Size is {self.board_size}.")
        print(f"The number of ships each side has is {self.num_ships}.")
        print(f"You will have {num_turns} turns.")
        print("Top left corner is row: 0, col 0\n")
        print("--LEGEND--")
        print("@ Is a ship")
        print("- Is a miss")
        print("X Is a hit\n")
        print("Good Luck!!!")
        self.player_board = Board(self.player_name, self.board_size, self.num_ships)
        self.computer_board = Board('PC', self.board_size, self.num_ships)
        self.player_board.display(misses=self.computer_board.misses, hits=self.computer_board.hits, hidden=False)
        self.computer_board.display(misses=self.player_board.misses, hits=self.player_board.hits)

# PLAYERS TURN
# Check if the player_guess is in computer_ships

    def user_play(self):
        print(f"You have used {self.num_turns_taken} out of {self.num_turns} turns")
        print(f"You have {self.num_turns - self.num_turns_taken} turns left")
        row = self.player_board.validate_coordinate("Please guess a row (or type 'Q' to quit/exit): \n", ['0', '1', '2', '3', '4', 'Q'])
        if row.upper() == "Q":
            return end_game()
        column = self.player_board.validate_coordinate("Please guess a column (or 'quit' to exit): \n", ['0', '1', '2', '3', '4', 'Q'])
        if column.upper() == "Q":
            return end_game()
        print("-" * 35)
        coordinate = (int(self.board_size) * int(row)) + int(column)
        if (coordinate in self.player_board.misses) or (coordinate in self.player_board.hits):
           print('You already guessed this coordinate')
        else:
            self.num_turns_taken = self.num_turns_taken + 1
            if coordinate in self.computer_board.ships:
                print(f"Congratulations {self.player_name} You hit a ship!")
                self.player_board.hits.append(coordinate)
                print("-" * 35)
            else:
                print(f"You missed {self.player_name}, try again")
                self.player_board.misses.append(coordinate)
                print("-" * 35)

# COMPUTERS TURN
# Check if computer_guess is in player_ships

    def computer_play(self):
        computer_guess = random.randint(0, 24)
        while (computer_guess in self.computer_board.misses) or (computer_guess in self.computer_board.hits):
            computer_guess = random.randint(0, 24)
        if computer_guess in self.player_board.ships:
            print("Computer hit one of your ships!")
            self.computer_board.hits.append(computer_guess)
            print("-" * 35)
        else:
            print("Computer missed your ships")
            self.computer_board.misses.append(computer_guess)
            print("-" * 35)

    def play(self):
        player_wins = False
        computer_wins = False
        while self.num_turns > self.num_turns_taken:
            self.user_play()
            self.computer_play()
            if len(self.computer_board.hits) == self.num_ships:
                print('Computer WINS!!')
                self.num_turns_taken = 10
                computer_wins = True
            if len(self.player_board.hits) == self.num_ships:
                print(f'{self.username} WINS!!')
                self.num_turns_taken = 10
                player_wins = True
            self.player_board.display(misses=self.computer_board.misses, hits=self.computer_board.hits, hidden=False)
            self.computer_board.display(misses=self.player_board.misses, hits=self.player_board.hits)
        if (computer_wins is False and player_wins is False):
            print('Game over, you ran out of turns')
            if len(self.player_board.hits) > len(self.computer_board.hits):
                print(f'{self.username} WINS with {len(self.player_board.hits)} hits!!')
            if len(self.player_board.hits) < len(self.computer_board.hits):
                print(f'Computer WINS with {len(self.computer_board.hits)} hits!!')
            if len(self.player_board.hits) == len(self.computer_board.hits):
                print(f'is a TIE!!')

def end_game():
    print("Do you want to play again?")
    print("(type Y to play again")
    play_again = str(input(" or any other key to quit):\n"))
    if play_again.upper() == "Y":
        play_game()
    else:
        print("Thankyou for playing. Goodbye!")
        return

def continue_game():
    print(f"Do you accept the challenge {player_name}?")
    print("(type Y to continue")
    play_again = str(input(" or any other key to quit):\n"))
    if play_again.upper() == "Y":
        return
    else:
        print("Thankyou for playing. Goodbye!")
        return

def play_game():
    num_turns_taken = 0
    while num_turns_taken < num_turns:
        print(f"{player_name}'s Board")
        display_player_board()

        print("\nComputers Board")
        display_computer_board()

        print("-" * 35)
        print(f"You have used {num_turns_taken} out of {num_turns} turns")
        print(f"You have {num_turns - num_turns_taken} turns left")

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
        num_turns_taken = num_turns_taken + 1
    



# MAIN CODE-------------------------------------------------------------------------------------------

if __name__ == "__main__":
    play_again = True
    while play_again:
        game = Game(board_size=5, num_ships=3)
        game.play()
        play_again = input('Press any key to play again, press q/Q to exit: ') not in ['q', 'Q']
    print('Thank you for playing')

