from munchkin.doors.door import Door


class Curse(Door):

    def __init__(self, name, target, description_effect):
        super().__init__(name)
        self.target = exec(target+'()')
        self.description_effect = description_effect

    def apply_effect(self, player):
        player.on_board

    def __str__(self):
        return super().__str__() + '\n Description Effect: ' + self.description_effect