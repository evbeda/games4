from ur_game.cell import Cell
from ur_game.token import Token


class Player:
    def __init__(self, shared=None):
        self.shared = shared
        self.initial = [Token() for _ in range(7)]
        self.start = [Cell() for _ in range(4)]

