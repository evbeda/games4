
class Treasure:

    def __init__(self, name, bonus, value, used_by=None, is_big=False):
        if bonus is None:
            bonus = 0
        self.name = name
        self.bonus = bonus
        self.value = value
        self.used_by = used_by
        self.is_big = is_big
