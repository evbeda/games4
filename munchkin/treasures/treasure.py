
class Treasure:

    def __init__(self, name, bonus, value, used_by=None, is_big=False):
        if bonus is None:
            bonus = 0
        self.name = name
        self.bonus = bonus
        self.value = value
        self.used_by = used_by
        self.is_big = is_big

    def __str__(self):
        if self.used_by is None:
            used_by_to_print = "all"
        else:
            used_by_to_print = self.used_by

        str_aux = "Name: {} | Bonus: {} | Value: {} | Used by: {} | Is big?: {} | ".format(self.name, self.bonus, self.value, used_by_to_print, self.is_big)
        return str_aux
