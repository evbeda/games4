space_free = '-'
space_invalid = 'X'
space_occupied = '0'


class SenkuGame(object):
    name = "Senku"
    __row = 7
    __col = 7

    def __init__(self):
        self._board = [[space_occupied for _ in range(self.__row)] for _ in range(self.__col)]

        for i in range(self.__row):
            if 2 > i or i > 4:
                for j in range(self.__col):
                    if 2 > j or j > 4:
                        self._board[i][j] = space_invalid
        self._board[3][3] = space_free

    # def next_turn(self):
    #     pass

    def play(self, initial_row, initial_col, final_row, final_col):
        try:
            self.validate_move(initial_row, initial_col, final_row, final_col)
        except ValueError:
            pass
        else:
            self.__move_piece(initial_row, initial_col, final_row, final_col)

    @property
    def board(self):
        head = [str(i) for i in range(self.__col)]
        horizontal_separator = ['=' for i in range(self.__col)]
        vertical_separator = '| '
        body = ''

        for index in range(len(self._board)):
            line = str(index) + vertical_separator + ' '.join(elem for elem in self._board[index])
            body += line + '\n'

        return ' ' * len(vertical_separator) \
               + ' '.join(head) \
               + '\n' \
               + ' + ' \
               + ' '.join(horizontal_separator) + '\n' \
               + body

    def validate_move(self, *positions):
        initial_row, initial_col, final_row, final_col = positions

        for pos in positions:
            if (
                    pos < 0 or
                    pos > 6 or
                    not self._board[initial_row][initial_col] == space_occupied or
                    not self._board[final_row][final_col] == space_free
            ):
                raise SenkuMovementOutOfRangeException('Value must be between 0 and 6')

        if initial_row == final_row and abs(initial_col - final_col) == 2:
            if self._board[initial_row][(initial_col + final_col) // 2] == space_occupied:
                return True
            else:
                raise SenkuInvalidMovementException(
                    "The position [{}, {}] must have a '0', but it has '{}'".format(
                        initial_row,
                        (initial_col + final_col) // 2,
                        self._board[initial_row][(initial_col + final_col) // 2],
                    )
                )

        if initial_col == final_col and abs(initial_row - final_row) == 2:
            if self._board[(initial_row + final_row) // 2][initial_col] == space_occupied:
                return True
            else:
                raise SenkuInvalidMovementException(
                    "The position [{}, {}] must have a '0', but it has '{}'".format(
                        initial_row,
                        (initial_col + final_col) // 2,
                        self._board[(initial_row + final_row) // 2][initial_col],
                    )
                )

        raise SenkuInvalidMovementException(
            "Only horizontal or vertical movements are allow"
        )

    def __move_piece(self, initial_row, initial_col, final_row, final_col):
        self._board[initial_row][initial_col] = space_free
        self._board[final_row][final_col] = space_occupied

        if initial_row == final_row:
            self._board[initial_row][(initial_col + final_col) // 2] = space_free

        if initial_col == final_col:
            self._board[(initial_row + final_row) // 2][final_col] = space_free

    def get_board(self):
        return self._board

    def set_board(self, arr_board):
        self._board = arr_board


class SenkuException(Exception):
    pass


class SenkuMovementOutOfRangeException(SenkuException):
    pass


class SenkuInvalidMovementException(SenkuException):
    pass



