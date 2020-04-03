from munchkin.treasures.treasure import Treasure


class Various(Treasure):

    def __init__(self, name, bonus, value, used_by=None, is_big=False, flee_bonus=0, cant_hands=0):
        super().__init__(name, bonus, value, used_by, is_big)
        self.flee_bonus = flee_bonus
        self.cant_hand = cant_hands

    def __str__(self):
        var = super().__str__()
        var = var + "Flee bonus: {} | Cant Hand: {} | ".format(self.flee_bonus, self.cant_hand)
        return var
