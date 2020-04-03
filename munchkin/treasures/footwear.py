from munchkin.treasures.treasure import Treasure


class Footwear(Treasure):

    def __init__(self, name, bonus, value, used_by=None, is_big=False, flee_bonus=0):
        super().__init__(name, bonus, value, used_by)
        self.flee_bonus = flee_bonus

    def __str__(self):
        my_var = super().__str__()

        my_var = my_var + "Flee bonus: {} | ".format(self.flee_bonus)
        return my_var
