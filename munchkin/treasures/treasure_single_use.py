from munchkin.treasures.treasure import Treasure


class TreasureSingleUse(Treasure):

    def __init__(self, name, bonus, group_effect, is_level_up, value, used_by=None, reroll_dice=False, flee_points=0, win_treasure=True, affect_other_player=False):
        super().__init__(name, bonus, value, used_by)
        self.group_effect = group_effect  # boolean, si la carta afecta al grupo que va a pelear
        self.is_level_up = is_level_up  # boolean, si la carta sube nivel
        self.reroll_dice = reroll_dice  # boolean, volver a lanzar el dado
        self.flee_points = flee_points  # puntos de huida
        self.win_treasure = win_treasure  # puede ganar tesoro
        self.affect_other_player = affect_other_player  # la carta afecta a otro jugador

    def __str__(self):
        if self.value is None:
            self.value = 0
        var = super().__str__()
        var = var + "Group effect: {} | Is level up: {} | Re-roll dice: {} | Flee points: {} | Win treasure: {} | Affect other player: {} | ".format(self.group_effect, self.is_level_up, self.reroll_dice, self.flee_points, self.win_treasure, self.affect_other_player)
        return var
