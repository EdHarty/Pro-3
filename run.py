import random

#import random variable generators.



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