class Senku(object):
    name = 'Senku'
    input_args = 1
    tablero = []

    def __init__(self):
        self.is_playing = True
        x, y = 7, 7
        self.tablero = [[0 for i in range(x)] for y in range(y)]
        for i in range(x):
            for j in range(y):
        self.tablero[0][0] = 'x'
        self.tablero[0][1] = 'x'
        self.tablero[1][1] = 'x'

    def next_turn(self):
        if self.is_playing:
            return 'Introduce next movement'
        else:
            return 'Game Over'

    def play(self, number):
        pass

    def board(self):
        for elem in self.tablero:
            print elem
