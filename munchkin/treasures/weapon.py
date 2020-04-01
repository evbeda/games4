from munchkin.treasures.treasure import Treasure


class Weapon(Treasure):

    def __init__(self, size, cant_hands, name, bonus, value, used_by = None, is_big = False):
        super().__init__(name, bonus, value, used_by)
        self.size = size
        self.cant_hands = cant_hands
