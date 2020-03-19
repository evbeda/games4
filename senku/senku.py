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
        if self.is_playing:
            return 'Introduce next movement'
        else:
            return 'Game Over'

    def play(self, initial_x, initial_y, final_x, final_y):
        if self.validate_move(initial_x, initial_y, final_x, final_y):
            self.__move_piece(initial_x, initial_y, final_x, final_y)

    @property
    def board(self):
        return '\n'.join(' '.join(elem) for elem in self._board)

    def validate_move(self, *positions):
        ## como mejora, deberiamos manejar excepciones para devolver un status y un msg
        initial_x, initial_y, final_x, final_y = positions

        for pos in positions:
            if ((pos < 0 or pos > 6)
                    or not self._board[initial_x][initial_y] == space_occupied
                    or not self._board[final_x][final_y] == space_free):
                return False

        if initial_x == final_x and abs(initial_y - final_y) == 2:
            if self._board[initial_x][(initial_y + final_y) // 2] == space_occupied:
                return True

        if initial_y == final_y and abs(initial_x - final_x) == 2:
            if self._board[(initial_x + final_x) // 2][initial_y] == space_occupied:
                return True
        return False

    def __move_piece(self, initial_x, initial_y, final_x, final_y):
        self._board[initial_x][initial_y] = space_free
        self._board[final_x][final_y] = space_occupied

        if initial_x == final_x:
            self._board[initial_x][(initial_y + final_y) // 2] = space_free

        if initial_y == final_y:
            self._board[(initial_x + final_x) // 2][final_y] = space_free

    def get_board(self):
        return self._board

    def set_board(self, arr_board):
        self._board = arr_board
