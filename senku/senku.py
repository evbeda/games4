space_free = '-'
space_invalid = 'X'
space_occupied = '0'


class Senku(object):
    name = 'Senku'

    def __init__(self):
        x, y = 7, 7
        self._board = [[space_occupied for _ in range(x)] for _ in range(y)]

        for i in range(7):
            if 2 > i or i > 4:
                for j in range(7):
                    if 2 > j or j > 4:
                        self._board[i][j] = space_invalid
        self._board[3][3] = space_free

    def next_turn(self):
        pass

    def play(self, initial_row, initial_col, final_row, final_col):
        if self.validate_move(initial_row, initial_col, final_row, final_col):
            self.__move_piece(initial_row, initial_col, final_row, final_col)

    @property
    def board(self):
        return '\n'.join(' '.join(elem) for elem in self._board)

    def validate_move(self, *positions):
        ## como mejora, deberiamos manejar excepciones para devolver un status y un msg
        initial_row, initial_col, final_row, final_col = positions

        for pos in positions:
            if ((pos < 0 or pos > 6)
                    or not self._board[initial_row][initial_col] == space_occupied
                    or not self._board[final_row][final_col] == space_free):
                return False

        if initial_row == final_row and abs(initial_col - final_col) == 2:
            if self._board[initial_row][(initial_col + final_col) // 2] == space_occupied:
                return True

        if initial_col == final_col and abs(initial_row - final_row) == 2:
            if self._board[(initial_row + final_row) // 2][initial_col] == space_occupied:
                return True
        return False

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


##crear nuestra propia jerarquia de errores