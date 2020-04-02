from ur_game.cell import Cell
from ur_game.player import Player
from random import randint


class UrGame:

    def __init__(self):
        shared = [Cell(False) for _ in range(8)]
        shared[3].set_special()
        self.players = [Player(shared) for _ in range(2)]

    @property
    def is_playing(self):
        for player in self.players:
            if len(player.final_stack) == 7:
                return False
        return True

    @staticmethod
    def roll_dices():
        return randint(0, 4)
