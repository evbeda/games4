from .tower import Tower
from .tower import InvalidMovement
from .tower import EmptyTower


class HanoiTowers:

    def __init__(self, cant_tokens):

        self.cant_tokens = cant_tokens
        self.towers = [Tower(cant_tokens), Tower(), Tower()]
        self.is_playing = True

    def next_turn(self):

        if (len(self.towers[2].tokens) == self.cant_tokens) or (len(self.towers[1].tokens) == self.cant_tokens):
            self.is_playing = False
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

    @property
    def board(self):
        tower_print = ""
        for tower in self.towers:
            tower_print += f"Tower {self.towers.index(tower)}:\n"
            for index in range(self.cant_tokens-1, -1, -1):
                tower_print += " |"
                if len(tower.tokens) > index:
                    for y in range(tower.tokens[index].size):
                        tower_print += "-"
                tower_print += "\n"
            tower_print += "\n"
        return tower_print




        """
        tallest = max(len(self.towers[0].tokens), len(self.towers[1].tokens), len(self.towers[2].tokens))
        board = ""
        for row in range(tallest, 0, -1):
            if len(self.towers[0].tokens) >= row:
                board += " {}  ".format(self.towers[0].tokens[row-1].size)
            else:
                board += "    "
            if len(self.towers[1].tokens) >= row:
                board += " {}  ".format(self.towers[1].tokens[row-1].size)
            else:
                board += "    "
            if len(self.towers[2].tokens) >= row:
                board += " {}  ".format(self.towers[2].tokens[row-1].size)
            else:
                board += "    "
            board += "\n"
        board += "=== === ==="
        return board
        """