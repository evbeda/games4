from ur_game.cell import Cell
from ur_game.player import Player
from random import randint


class UrGame:

    def __init__(self):
        shared = [Cell() for _ in range(8)]
        shared[3].set_special()
        self.players = [Player(shared, _) for _ in range(2)]
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
    
    @property
    def board(self):
        board = ""
        board += self.players[0].__str__() + "\n"
        board += self.__str__() + "\n"
        board += self.players[1].__str__()
        return board

    @staticmethod
    def roll_dices():
        dice1 = randint(0, 1)
        dice2 = randint(0, 1)
        dice3 = randint(0, 1)
        dice4 = randint(0, 1)
        return dice1 + dice2 + dice3 + dice4

    def __shared_arr_str(self):
        arr_str = "["
        player = self.players[0]
        index = 5
        for cell in player.shared:
            if cell.is_empty and cell.is_special and index < 12:
                arr_str += " *{},".format(index)
            elif cell.is_empty and not cell.is_special and index < 12:
                arr_str += " {},".format(index)
            elif index == 12 and cell.is_empty:
                arr_str += " {}".format(index)
            else:
                arr_str += " {},".format(cell.__str__())
            index += 1
        arr_str += "]"
        return arr_str

    def __str__(self):
        board_str = ""
        board_str += "-" * 36 + "\n"
        board_str += "Special cells marked with '*'\n"
        board_str += self.players[0].initial_and_final_arr_str() + "\n"
        board_str += self.__shared_arr_str() + "\n"
        board_str += self.players[1].initial_and_final_arr_str() + "\n"
        board_str += "-" * 36
        return board_str

