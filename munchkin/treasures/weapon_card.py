from munchkin.treasures.treasure import Treasure


class Weapon(Treasure):

    def __init__(self, name, bonus, size, value, use_by):
        super().__init__()
        self.type_treasure = "Weapon"
        self.name = name
        self.bonus = bonus
        self.size = size
        self.value = value
        self.use_by = use_by
