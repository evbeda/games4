from munchkin.treasures.treasure import Treasure


class Treasure_single_use(Treasure):

    def __init__(self, name, bonus, group_effect, is_level_up, value, used_by=None ):
        super().__init__(name, bonus, value, used_by)
        self.group_effect = group_effect # boolean, si la carta afecta al grupo que va a pelear
        self.is_level_up = is_level_up # boolean, si la carta sube nivel
