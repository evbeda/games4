
Monsters = {'name':'Chupacabras','level':8,'level_add':1,'treasures':2}
class Monstruo:
    def __init__(self,name,level,treasures,level_add):
        self._name = name
        self._level = level
        self._treasures = treasures
        self._level_add = level_add

    @property
    def level(self):
        return self._level

    @property
    def treasures(self):
        return self._treasures

    @property
    def treasures(self):
        return self._level_add
