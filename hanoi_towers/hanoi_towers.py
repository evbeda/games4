from .tower import Tower
from .tower import InvalidMovement
from .tower import EmptyTower


class HanoiTowers:

    def __init__(self, cant_tokens):

        self.cant_tokens = cant_tokens
        self.tower1 = Tower(cant_tokens)
        self.tower2 = Tower()
        self.tower3 = Tower()

    def next_turn(self):

        if (len(self.tower3.tokens) == self.cant_tokens) or (len(self.tower2.tokens) == self.cant_tokens):
            return "You won"
        else:
            return "Plase make your move"

    def play(self, source_tower, target_tower):

        try:
            my_token = source_tower.remove_token()
            target_tower.insert_token(my_token)
        except InvalidMovement:
            source_tower.insert_token(my_token)
            return "Invalid move"
        except EmptyTower:
            return "Empty tower"
