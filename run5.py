import random

GRID_SIZE = 10

# Ships and sizes
ships = {
    'Destroyer': 2,
    'Submarine': 3,
    'Battleship': 4
}

def random_row():
    return random.randint(0, GRID_SIZE - 1)

def random_col():
    return random.randint(0, GRID_SIZE - 1)

def place_ship(ship, size, grid):
    while True:
        row = random_row()
        col = random_col()

        is_vertical = random.choice([True, False])

        if is_vertical:
            if row + size > GRID_SIZE:
                continue

            if '.' not in [grid[row + i][col] for i in range(size)]:
                continue

            for i in range(size):
                grid[row + i][col] = ship[0]
        else:
            if col + size > GRID_SIZE:
                continue

            if '.' not in [grid[row][col + i] for i in range(size)]:
                continue

            for i in range(size):
                grid[row][col + i] = ship[0]

        break

    return True

def place_ships(grid):
    for ship, size in ships.items():
        while True:
            placed = place_ship(ship, size, grid)
            if placed:
                break
    return grid

def fire(row, col, grid):
    mark = grid[row][col]
    if mark == 'X' or mark == '-':
        print("\nYou've already fired at this location. Try somewhere new!")
        return
    elif mark != '.':
        print(f"\nHit! {mark} ship segment destroyed.")
        grid[row][col] = 'X'
        return mark
    else:
        print("\nYou missed!")
        grid[row][col] = '-'
        return False

def print_grid(grid, fog_of_war=True):
    print('  ' + ' '.join(map(str, range(GRID_SIZE))))
    for i, row in enumerate(grid):
        if fog_of_war:
            row = ['.' if cell != 'X' else 'X' for cell in row]
        print(f'{i} ' + ' '.join(row))

def print_help():
    print("Welcome to Battleship!")
    print("To play the game, enter the row and column number of the square you want to fire at.")
    print("The row and column numbers are numbered from 0 to 9, starting from the top left corner of the grid.")
    print("You will have 10 turns to sink all of the enemy ships.")
    print("If you sink all of the enemy ships before you run out of turns, you win!")
    print("Good luck!")

def main():
    print_help()

    # Place player ships
    player_grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]
    player_grid = place_ships(player_grid)

    # Place enemy ships
    enemy_grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]
    enemy_grid = place_ships(enemy_grid)

    ships_remaining = len(ships)

    while ships_remaining > 0:
        print("(Type 'quit' to exit the game)")

        # Get input
        action = input("Enter row (or 'quit' to exit), followed by column to fire at: ")
        if action.lower().strip() == 'quit':
            break

        coordinates = action.split()
        if len(coordinates) != 2:
            print("\nInvalid coordinates, please re-enter.")
            continue

        try:
            row, col = map(int, coordinates)
            if row < 0 or row >= GRID_SIZE or col < 0 or col >= GRID_SIZE:
                print("\nInvalid coordinates, retry.")
                continue
        except ValueError:
            print("\nInvalid input, please enter row and column as integers.")
            continue

        hit_ship = fire(row, col, enemy_grid)

        if hit_ship:
            # If all ship segments are hit, mark the ship as destroyed
            ship_name = [name for name, size in ships.items() if name[0] == hit_ship][0]
            if hit_ship not in ''.join([''.join(row) for row in enemy_grid]):
                print(f"\nYou have destroyed the enemy's {ship_name}!")
                ships_remaining -= 1

        print("\nYour Grid:")
        print_grid(player_grid, fog_of_war=False)
        print("\nEnemy Grid:")
        print_grid(enemy_grid)

    if action.lower().strip() == 'quit':
        print("\nYou chose to quit the game.")
    elif ships_remaining != 0 and action.lower().strip() != "quit":
        print("\nAll your turns are over! You did not shoot down all enemy ships!")
    else:
        print("\nAll enemy ships destroyed! You win!")

if __name__ == "__main__":
    main()