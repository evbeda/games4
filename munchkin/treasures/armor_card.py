from munchkin.treasures.treasure import Treasure

class Armor(Treasure):

    def __init__(self, name, bonus, part, value, use_by):
        super().__init__()
        self.type_treasure = "Armor"
        self.name = name
        self.bonus = bonus
        self.part = part
        self.value = value
        self.use_by = use_by