from munchkin.treasures.treasure import Treasure


class Weapon(Treasure):

    def __init__(self, cant_hands, name, bonus, value, used_by=None, is_big=False):
        super().__init__(name, bonus, value, used_by, is_big)
        self.cant_hands = cant_hands

    def __str__(self):
        var = super().__str__()
        var = var + "Cant hands: {} | ".format(self.cant_hands)
        return var
