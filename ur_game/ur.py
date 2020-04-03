from ur_game.cell import Cell
from ur_game.player import Player
from random import randint


class UrGame:

    def __init__(self):
        shared = [Cell() for _ in range(8)]
        shared[3].set_special()
        self.players = [Player(shared) for _ in range(2)]
        self.active_player = None

    def next_turn(self):
        if self.active_player is not None and self.active_player.addition_turn:
            self.active_player.addition_turn = False
        else:    
            for player in self.players:
                if self.active_player != player:
                    self.active_player = player
                    break
        player_name = None
        if self.active_player == self.players[0]:
            player_name = "Player 1"
        else:
            player_name = "Player 2"
        return f"Its {player_name} Turn"

    @property
    def is_playing(self):
        for player in self.players:
            if len(player.final_stack) == 7:
                return False
        return True

    @staticmethod
    def roll_dices():
        dice1 = randint(0, 1)
        dice2 = randint(0, 1)
        dice3 = randint(0, 1)
        dice4 = randint(0, 1)
        return dice1 + dice2 + dice3 + dice4
