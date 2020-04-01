from munchkin.treasures.treasure import Treasure


class TreasureSingleUse(Treasure):

    def __init__(self, name, bonus, group_effect, is_level_up, value, used_by=None, reroll_dice= False):
        super().__init__(name, bonus, value, used_by)
        self.group_effect = group_effect  # boolean, si la carta afecta al grupo que va a pelear
        self.is_level_up = is_level_up  # boolean, si la carta sube nivel
        self.reroll_dice = reroll_dice  # boolean, volver a lanzar el dado
