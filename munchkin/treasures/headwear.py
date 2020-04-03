from munchkin.treasures.treasure import Treasure


class Headwear(Treasure):

    def __init__(self, name, bonus, value, used_by=None, is_big=False, extra_bonus=0, extra_used_by=None):
        super().__init__(name, bonus, value, used_by, is_big)
        self.extra_bonus = extra_bonus
        self.extra_used_by = extra_used_by

    def __str__(self):
        var = super().__str__()
        if self.extra_used_by is None:
            extra_used_by_print = "Nobody"
        else:
            extra_used_by_print = self.extra_used_by

        var = var + "Extra bonus: {} | Extra used by: {} | ".format(self.extra_bonus, extra_used_by_print)
        return var
