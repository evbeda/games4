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

    def play(self, source, target):

        try:
            source = int(source)
            target = int(target)
            self.validate_input(source, target)
            my_token = self.towers[source].remove_token()
            self.towers[target].insert_token(my_token)
        except InvalidMovement:
            self.towers[source].insert_token(my_token)
            return "Invalid move"
        except EmptyTower:
            return "Empty tower"
        except ValueError:
            return "Error: enter only integers"
        except SameTowerException:
            return "Error: the towers must be different"
        except NotValidTowerIndexException:
            return f"Error: enter numbers between 0 and {len(self.towers)-1}"

    def validate_input(self, source, target):
        if source == target:
            raise SameTowerException
        try:
            self.towers[source]
            self.towers[target]
        except IndexError:
            raise NotValidTowerIndexException
        return True
    
    @property
    def board(self):
        tower_print = ""
        for tower in self.towers:
            tower_print += f"Tower {self.towers.index(tower)}:\n"
            for index in range(self.cant_tokens-1, -1, -1):
                tower_print += " |"
                if len(tower.tokens) > index:
                    for _ in range(tower.tokens[index].size):
                        tower_print += "-"
                tower_print += "\n"
            tower_print += "\n"
        return tower_print


class SameTowerException(Exception):
    pass


class NotValidTowerIndexException(Exception):
    pass