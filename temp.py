"""
From Code institute
"""

from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. Sets board size, the number of ships, 
    the player's name and the board type (player board or computer)
    has methods for adding ships and guesses and printing the board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x] [y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"
        
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add more ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)

def valid_coordinates(x, y, board):
    """
    Validates the coordinates that have been input to make sure that they haven't already been guessed and  that they're not outside the scope of our board.
    """
    pass


def populate_board(board):
    pass


def make_guess(board):
    """
    Processes the guesses
    """
    pass


def play_game(computer_board, player_board):
    pass



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
    player_name = input("Please enter your name: \n")
    print("-" * 35)


    computer_board = Board(size, num_ships, "Computer", type="computer")    # class instance for computer_board
    player_board = Board(size, num_ships, player_name, type="player")       # Class instance for player board

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)


new_game()







        
    
