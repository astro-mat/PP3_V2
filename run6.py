import random

"""
Game Constants
"""

GRID_SIZE = 10 #will represent the 10x10 dimension of our board.
SHIPS = {'Destroyer': 2, 'Submarine': 3, 'Battleship': 4} #will hold the ship names mapped to their sizes.

"""
Create two 10x10 grids with list comprehension for the computer and the player.
populated with dots to indicate empty squares
"""

player_grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]
enemy_grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]

"""
Randomly place ships onto players grid
"""


def random_row():
  return random.randint(0, GRID_SIZE - 1)

def random_col():
  return random.randint(0, GRID_SIZE - 1)


"""
Function to position a single ship
"""
def place_ship(ship, size, grid):

  # Randomly generate row, col index for head of ship
  row = random_row()
  col = random_col()

  # Randomly choose vertical or horizontal orientation
  is_vertical = random.choice([True, False])

  if is_vertical:
    if row + size > GRID_SIZE:
      return False

    for i in range(size):
      grid[row+i][col] = ship[0]
  else:
    if col + size > GRID_SIZE:
      return False

    for i in range(size):
      grid[row][col+i] = ship[0]

  return True

"""
Populate the grid by looping through place_ships untill each one fits
"""

def place_ships(grid):
    for ship, size in ships.items():
        while True:
            placed = place_ship(ship, size, grid)
            if placed:
                break
    return grid


"""
PLAYING THE GAME
"""

"""
Player moves
Impliment the logic for each players turn
1.Getting coordinates input for strike.
2.Checking for a hit or miss.
3.Updating enemy grid accordingly.
"""
def player_move():

  print("Enter row and column to strike: ")

  row, col = input().split()
  row, col = int(row), int(col)

  mark = enemy_grid[row][col]

  if mark == 'X' or mark == '-':
    print("You already struck here!")
    return

  if mark == '.':
    print("You missed!")
    enemy_grid[row][col] = '-'
  else:
    print("Hit!")
    enemy_grid[row][col] = 'X'

"""
Enemy moves
"""

def enemy_move():

  row = random_row()
  col = random_col()

  mark = player_grid[row][col]

  if mark == 'X' or mark == '-':
    return

  if mark == '.':
    print("Enemy missed!")
    player_grid[row][col] = '-'
  else:
    print("Enemy hit!")
    player_grid[row][col] = 'X'

