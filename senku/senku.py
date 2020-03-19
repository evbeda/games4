class Senku(object):
    name = 'Senku'
    input_args = 1
    board = []

    def __init__(self):
        self.is_playing = True
        x, y = 7, 7
        self.board = [['0' for i in range(7)] for y in range(7)]

        for i in range(7):
            if 2 > i or i > 4:
                for j in range(7):
                    if 2 > j or j > 4:
                        self.board[i][j] = 'x'
        self.board[3][3] = '-'

    def next_turn(self):
        if self.is_playing:
            return 'Introduce next movement'
        else:
            return 'Game Over'

    def play(self, number):
        pass

    def show_board(self):
        return '\n'.join(' '.join(elem) for elem in self.board)
