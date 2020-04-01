from ur_game.cell import Cell
from ur_game.token import Token


class Player:
    def __init__(self, shared=None):
        self.shared = shared
        self.initial = [Token(i) for i in range(7)]
        self.final_stack = []
        self.start = [Cell() for _ in range(4)]
        self.finish = [Cell() for _ in range(2)]
