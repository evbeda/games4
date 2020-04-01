from munchkin.treasures.treasure import Treasure


class Various(Treasure):

    def __init__(self, name, bonus, value, used_by=None, is_big=False, flee_bonus=0, cant_hands=0):
        super().__init__(name, bonus, value, used_by, is_big)
