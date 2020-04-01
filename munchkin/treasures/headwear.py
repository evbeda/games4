from munchkin.treasures.treasure import Treasure

class Headwear(Treasure):

    def __init__(self, name, bonus, value, used_by = None, is_big = False, extra_bonus = None, extra_used_by = None):
        super().__init__(name, bonus, value, used_by, is_big)
        self.extra_bonus = extra_bonus
        self.extra_used_by = extra_used_by
