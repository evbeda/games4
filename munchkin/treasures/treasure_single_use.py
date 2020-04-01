from munchkin.treasures.treasure import Treasure


class TreasureSingleUse(Treasure):

    def __init__(self, name, bonus, group_effect, is_level_up, value, used_by=None, reroll_dice= False, flee_points=0, win_treasure=True):
        super().__init__(name, bonus, value, used_by)
        self.group_effect = group_effect  # boolean, si la carta afecta al grupo que va a pelear
        self.is_level_up = is_level_up  # boolean, si la carta sube nivel
        self.reroll_dice = reroll_dice  # boolean, volver a lanzar el dado
        self.flee_points = flee_points  # puntos de huida
        self.win_treasure = win_treasure  # puede ganar tesoro
