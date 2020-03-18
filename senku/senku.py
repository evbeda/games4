class Senku(object):

    name = 'Senku'
    input_args = 1

    def __init__(self):
        self.is_playing = True

    def next_turn(self):
        if self.is_playing:
            return 'Introduce next movement'
        else:
            return 'Game Over'

    def play(self, number):

    @property
    def board(self):
        return str(self.board)