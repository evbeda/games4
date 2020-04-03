from ur_game.cell import Cell
from ur_game.player import Player, InvalidMovementException, OutOfBoardException
from random import randint


class IsNotOneCharacter(Exception):
    pass


class UrGame:

    def __init__(self):
        shared = [Cell() for _ in range(8)]
        shared[3].set_special()
        self.players = [Player(shared) for _ in range(2)]
        self.active_player = None
        self.dice_value = None

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

    def play(self, source):
        try:
            source = int(source)
            self.validate_number_lenght(source)
            self.dice_value = self.roll_dices()
            self.active_player.move_token(self.dice_value, source)
            if(self.active_player == 7):
                return 'You won'
            return "Token moved successfully"
        except InvalidMovementException:
            return "You dont have more Tokens"
        except OutOfBoardException:
            return "Out of board"
        except ValueError:
            return "The value {} is not a number".format(source)
        except IsNotOneCharacter:
            return "Only one number is expected, you are introducing {} character".format(len(source))

    @staticmethod
    def roll_dices():
        dice1 = randint(0, 1)
        dice2 = randint(0, 1)
        dice3 = randint(0, 1)
        dice4 = randint(0, 1)
        return dice1 + dice2 + dice3 + dice4

    def validate_number_lenght(self, source):
        if len(str(source)) > 1:
            raise IsNotOneCharacter("Only one number is expected, you are introducing {} character".format(len(source)))
