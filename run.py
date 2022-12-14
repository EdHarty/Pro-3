import random
import time
import sys


class Board:

    """
    Sets player board, game board and size of board.
    Sets ships sizes.
    """

    def __init__(self, player):
        # Player board
        self.player = player

        # The game board
        self.board = [[0 for bd in range(10)] for r in range(10)]

        # Board that shows positions that has been attacked.
        self.board_attacked = [[0 for bd in range(10)] for r in range(10)]

        # The battleships.
        self.ships = []

        # Different sized battleships.
        self.append_ship(4)
        self.append_ship(3)
        self.append_ship(3)
        self.append_ship(2)
        self.append_ship(2)
        self.append_ship(2)
        self.append_ship(1)
        self.append_ship(1)
        self.append_ship(1)
        self.append_ship(1)

    def __repr__(self):

        repr = '\nPlayer Board:\n'

        repr += '\n  A B C D E F G H I J\n'

        for row in range(10):
            repr += f'{row} '

            for col in range(10):

                if self.board[row][col] == 0:
                    repr += '-'
                else:
                    repr += 'x'

                if col < 9:
                    repr += ' '

            if row < 9:
                repr += '\n'

        return repr

    # Add a battleship.
    def append_ship(self, size):
        """
        Adds ship randomly and positions ship in
        particular direction.
        """

        # Create a battleship.
        ship = Battleship(size)

        # Ship placement.
        min_row = size - 1
        min_col = size - 1
        max_row = 10 - size
        max_col = 10 - size

        placed_ship = False

        while not placed_ship:

            # Randomize ship placement.
            set_row = random.randint(min_row, max_row)
            set_col = random.randint(min_col, max_col)

            current_row, current_col = set_row, set_col

            # Ship orientation.
            location = random.randint(1, 4)

            placed_ship = True

            # Check to see if area is occupied already.
            for i in range(0, size):

                if not self.check_area(current_row, current_col):
                    placed_ship = False
                    break

                # Up
                if location == 1:
                    current_row -= 1

                # Down
                elif location == 2:
                    current_row += 1

                # Right
                elif location == 3:
                    current_col += 1

                # Left
                else:
                    current_col -= 1

            # If area is free plot the ship.
            if placed_ship:

                current_row, current_col = set_row, set_col

                for i in range(0, size):

                    # Area is taken.
                    self.board[current_row][current_col] = 1

                    # ship area occupied.
                    ship.add_section(current_row, current_col)

                    # Up
                    if location == 1:
                        current_row -= 1

                    # Down
                    elif location == 2:
                        current_row += 1

                    # Right
                    elif location == 3:
                        current_col += 1

                    # Left
                    else:
                        current_col -= 1

                # Add this ship to the board
                self.ships.append(ship)

    # Remove a battleship from the board
    def minus_ship(self, ship):
        """
        Removes a battleship from the board.
        """
        self.ships = [x for x in self.ships if x != ship]

    # Check if area is occupied.
    def check_area(self, row, col):
        """
        This is to check if areas on the board are occupied.
        """

        # Check surrounding area.
        for r in range(row - 1, row + 2):
            for bd in range(col - 1, col + 2):
                try:

                    # If area is occupied, return False.
                    if self.board[r][bd] == 1:
                        return False

                except IndexError:
                    pass

        # If not occupied, return True
        return True

    # Attack specific coordinates.
    def attack(self, coordinates):
        """
        Attack specific coordinates and the outcome of the attack.
        """

        if self.player == 0:
            print(f'\nYour enemy launches an attack {coordinates}!')
        else:
            print(f'\nYou launch an attack {coordinates}!')

        # Break between turns.
        time.sleep(2)

        # Check if position has been attacked.
        if self.board_attacked[coordinates.row][coordinates.col]:
            print('\nThat position has already been attacked!')

        # If the area contains a ship.
        elif self.board[coordinates.row][coordinates.col]:

            print('\nDirect Hit!')

            # Identify ship that was hit.
            for ship in self.ships:

                if ship.minus_section(coordinates.row, coordinates.col):

                    # If ship is sunk.
                    if ship.is_destroyed():

                        # Remove ship.
                        self.minus_ship(ship)

                        # If no more ships.
                        if not self.ships:

                            # Winner/Loser.
                            if self.player == 0:
                                print('\nGame over! Player ships destroyed')
                            else:
                                print('\nVictory! Enemy ships destroyed')

                            # To exit the game.
                            sys.exit(0)

                        # If ships still remain.
                        else:

                            print('\nBattleship Destroyed!', end=' ')

                            if self.player == 0:
                                print(f'You have {len(self.ships)} ship(s) remaining on the board.')
                            else:
                                print(f'Your enemy has {len(self.ships)} ship(s) remaining on the board.')

                    break

            # Mark the area as empty.
            self.board[coordinates.row][coordinates.col] = 0

        # If the area doesn't contain a ship
        else:
            print('\nMiss!')

        self.board_attacked[coordinates.row][coordinates.col] = 1

        time.sleep(2)


class Battleship:
    """
    Create a new battleship in the free areas
    on the board.
    """

    # Create a new Battleship object.
    def __init__(self, size):
        self.size = size
        self.sections = []

    # Add a section to this ship's list of sections.
    def add_section(self, row, col):
        """
        Create a new battleship object and add a section.
        to this ship's list of sections.
        """
        self.sections.append([row, col])

    # Remove a section from this ship's list of sections.
    def minus_section(self, row, col):
        """
        Remove a section from this ship's list of sections.
        """

        target_section = [row, col]

        # Remove the target section if it exists.
        for section in self.sections:
            if section == target_section:
                self.sections = [bd for bd in self.sections if bd != target_section]

                # Return True if the target section was found and removed.
                return True

        # Return False if the target section was not found
        return False

    # If ship sank.
    def is_destroyed(self):
        """
        If battleship has been destroyed.
        """

        # Return True if the ship has no remaining areas, otherwise return False
        return not bool(self.sections)


class ErrorInvalid(Exception):
    pass


def get_move_from_user(board):
    """
    Display player's board and options to target
    enemy or quit the game.
    """

    # Loop while receiving player input.
    while True:

        # Show the player's board.
        print(board)

        user_input = input('\nSelect a target on your enemy\'s board (example: A5) (\'quit\' to end game): ')

        # Turn lowercase to uppercase.
        user_input = user_input.upper()

        # If player exits the game.
        if user_input == 'QUIT':
            print('\nQuitting game. Good-bye!')
            sys.exit(0)

        # Limit input length to 2 characters.
        if len(user_input) != 2:
            print('\nYou must only have 2 characters (example: A5)')
            continue

        try:
            return Coordinates(user_input[0], user_input[1])
        except ErrorInvalid:
            continue


class Enemy:
    """
    Logs previous attacks so as no to repeat those attacks.
    """

    def __init__(self):

        # log of previous turns so as not to repeat.
        self.board = [[0 for bd in range(10)] for r in range(10)]

    # Position computer will attack.
    def generate_move(self):
        """
        Creates random area to attack.
        """

        found_coordinates = False

        while not found_coordinates:

            # Random position attacked.
            set_row = random.randint(0, 9)
            set_col = random.randint(0, 9)

            # To see if position hasn't been attacked.
            if not self.board[set_row][set_col]:

                # Log position as already attacked.
                self.board[set_row][set_col] = 1

                found_coordinates = True

        chosen_coordinates = Coordinates(set_col, set_row)

        return chosen_coordinates


class Coordinates:

    """
    Validate the column and row arguments.
    """

    def __init__(self, col, row):

        # To validate column argument.
        if type(col) is int:
            if col < 0 or col > 9:
                print('\nColumn must be either integer (0-9) or string (A-J).')
                raise ErrorInvalid()

        # If player selects column.
        elif type(col) is str:
            if col not in 'ABCDEFGHIJ':
                print('\nThe first character must be a letter from A-J.')
                raise ErrorInvalid()

            # Express column as integer.
            if col == 'A':
                col = 0
            elif col == 'B':
                col = 1
            elif col == 'C':
                col = 2
            elif col == 'D':
                col = 3
            elif col == 'E':
                col = 4
            elif col == 'F':
                col = 5
            elif col == 'G':
                col = 6
            elif col == 'H':
                col = 7
            elif col == 'I':
                col = 8
            else:
                col = 9

        # Validate the row argument
        if type(row) is int:
            if row < 0 or row > 9:
                print('\nRow must be an integer (0-9).')
                raise ErrorInvalid()

        # If player selects row.
        elif type(row) is str:
            if row not in '0123456789':
                print('\nThe second character must be a number 0-9.')
                raise ErrorInvalid()

            row = int(row)

        # If input is correct, place the points.
        self.col = col
        self.row = row

    def __repr__(self):

        if self.col == 0:
            return 'A' + str(self.row)
        elif self.col == 1:
            return 'B' + str(self.row)
        elif self.col == 2:
            return 'C' + str(self.row)
        elif self.col == 3:
            return 'D' + str(self.row)
        elif self.col == 4:
            return 'E' + str(self.row)
        elif self.col == 5:
            return 'F' + str(self.row)
        elif self.col == 6:
            return 'G' + str(self.row)
        elif self.col == 7:
            return 'H' + str(self.row)
        elif self.col == 8:
            return 'I' + str(self.row)
        else:
            return 'J' + str(self.row)


if __name__ == "__main__":

    print('\nWelcome to Battleship!')

    # Generate a board for both players (0 = user, 1 = cpu)
    player_1_board = Board(0)
    player_2_board = Board(1)

    # Generate opponent for the player to compete against
    enemy = Enemy()

    # Main game loop
    while True:

        # Get a target position from the user
        target_coordinates = get_move_from_user(player_1_board)

        # Attack the enemies board at the given position
        player_2_board.attack(target_coordinates)

        # Enemy launches attack
        target_coordinates = enemy.generate_move()

        # Attack the user's board at the given position
        player_1_board.attack(target_coordinates)
