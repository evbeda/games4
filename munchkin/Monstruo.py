
Monsters={'name':'Chupacabras','level':8,'level_add':1,'treasures':2}
class Monstruo :
    def __init__(self) :
        self._level = Monsters['level']
        self._treasures = Monsters['treasures']
    
    @property
    def get_level(self):
        return self._level
    @property
    def get_treasures(self):
        return self._treasures
    
