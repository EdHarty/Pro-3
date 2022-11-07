import random



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


            
        
