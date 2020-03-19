class Senku(object):
    name = 'Senku'
    board = []
    space_free = '-'
    space_invalid = 'X'
    space_occupied = '0'

    def __init__(self):
        self.is_playing = True
        x, y = 7, 7
        self.board = [[self.space_occupied for i in range(x)] for j in range(y)]

        for i in range(7):
            if 2 > i or i > 4:
                for j in range(7):
                    if 2 > j or j > 4:
                        self.board[i][j] = self.space_invalid
        self.board[3][3] = self.space_free

    def next_turn(self):
        if self.is_playing:
            return 'Introduce next movement'
        else:
            return 'Game Over'

    def play(self, initial_x, initial_y, final_x, final_y):
        if self.validate_move(initial_x, initial_y, final_x, final_y):
            self.move_piece(initial_x, initial_y, final_x, final_y)

    def show_board(self):
        return '\n'.join(' '.join(elem) for elem in self.board)

    def validate_move(self, *positions):
        initial_x, initial_y, final_x, final_y = positions

        for pos in positions:
            if (pos < 0 or pos > 6) or not self.board[initial_x][initial_y] == self.space_occupied or not self.board[final_x][final_y] == self.space_free:
                return False

        if initial_x == final_x and abs(initial_y - final_y) == 2:
            if self.board[initial_x][initial_y + (final_y - initial_y)] == self.space_free:
                return True

        if initial_y == final_y and abs(initial_x - final_x) == 2:
            if self.board[initial_x + (final_x - initial_x)][initial_y] == self.space_free:
                return True
        return False

    def move_piece(self, initial_x, initial_y, final_x, final_y):
        self.board[initial_x][initial_y] = self.space_free
        self.board[final_x][final_y] = self.space_occupied

        if initial_x == final_x:
            self.board[initial_x][(initial_y + final_y) // 2] = self.space_free

        if initial_y == final_y:
            self.board[(initial_x + final_x) // 2][final_y] = self.space_free
