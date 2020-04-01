from ur_game.cell import Cell
from ur_game.player import Player


class UrGame:

    def __init__(self):
        shared = [Cell() for _ in range(8)]
        self.players = [Player(shared) for _ in range(2)]


