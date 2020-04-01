from munchkin.treasures.treasure import Treasure

class Footwear(Treasure):

    def __init__(self, name, bonus, value, used_by = None, is_big = False, flee_bonus = 0):
        super().__init__(name, bonus, value, used_by)
