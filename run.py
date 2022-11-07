import random
import time
import sys



class Board:

    """
    Sets player board, game board and size of board.
    Sets ships sizes.
    """

    def __init__(self, player):

        self.player = player

        self.board = [[0 for bd in range(10)] for r in range(10)]

        self.board_attacked = [[0 for bd in range(10)] for r in range(10)]

        self.ships = []

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

    def append_ship(self, size):
        """
        Adds ship randomly and positions ship in
        particular direction.
        """

        ship = Battleship(size)

        min_row = size - 1
        min_col = size - 1
        max_row = 10 - size
        max_col = 10 - size

        placed_ship = False

        while not placed_ship:

            set_row = random.randint(min_row, max_row)
            set_col = random.randint(min_col, max_col)

            current_row, current_col = set_row, set_col
            
            location = random.randint(1, 4)

            placed_ship = True

            for i in range(0, size):

                if not self.check_area(current_row, current_col):
                    placed_ship = False
                    break

                if location == 1:
                    current_row -= 1

                elif location == 2:
                    current_row += 1

                elif location == 3:
                    current_col += 1

                else:
                    current_col -= 1

            if placed_ship:

                current_row, current_col = set_row, set_col

                for i in range(0, size):

                    self.board[current_row][current_col] = 1

                    ship.add_section(current_row, current_col)

                    if location == 1:
                        current_row -= 1

                    elif location == 2:
                        current_row += 1

                    elif location == 3:
                        current_col += 1

                    else:
                        current_col -= 1

                self.ships.append(ship)

    def minus_ship(self, ship):
        """
        Removes a battleship from the board.
        """
        self.ships = [x for x in self.ships if x != ship]

    def check_area(self, row, col):
        """
        This is to check if areas on the board are occupied.
        """

        for r in range(row - 1, row + 2):
            for bd in range(col - 1, col + 2):
                try:

                    if self.board[r][bd] == 1:
                        return False

                except IndexError:
                    pass

        return True

    def attack(self, coordinates):
        """
        Attack specific coordinates and the outcome of the attack.
        """

        if self.player == 0:
            print(f'\nYour enemy launches an attack {coordinates}!')
        else:
            print(f'\nYou launch an attack {coordinates}!')

        time.sleep(2)

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

                            print('\nBattleship Desroyed!', end=' ')

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

        # Return True if the ship has no remaining areas,
        #  otherwise return False
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


class Enemy:
    """
    Logs previous attacks so as no to repeat those attacks.
    """

    def __init__(self):

        # log of previous turns so as not to repeat.
        self.board = [[0 for bd in range(10)] for r in range(10)]

    # Position under attack.
    def generate_move(self):
        """
        Creates random area to attack.
        """

        found_coordinates = False

        while not found_coordinates:

           
        
