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
        self.validate_move(initial_x, initial_y, final_x, final_y)
        pass

    def show_board(self):
        return '\n'.join(' '.join(elem) for elem in self.board)

    def validate_move(self, *positions):
        initial_x, initial_y, final_x, final_y = positions

        for pos in positions:
            if not 0 < pos < 7 and not self.board[initial_x][initial_y] == self.space_occupied and not self.board[final_x][final_y] == self.space_free
                return False


        if self.board[final_x][final_y] != self.space_free:
            return False


