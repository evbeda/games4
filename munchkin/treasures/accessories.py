from munchkin.treasures.treasure import Treasure

class Accessories(Treasure):

    def __init__(self, name, bonus, value, used_by = None, is_big = False):
        super().__init__(name, bonus, value, used_by, is_big)