from munchkin.doors.door import Door


class Monster(Door):

    def __init__(self, name, power, treasures, level_add):
        self._name = name
        self._power = power
        self._treasures = treasures
        self._level_add = level_add
        # bonus
        # who_bonus
        # level_lost
        # object_lost
        # who_object_lost

    @property
    def name(self):
        return self._name

    @property
    def power(self):
        return self._power

    @property
    def treasures(self):
        return self._treasures

    @property
    def level_add(self):
        return self._level_add
