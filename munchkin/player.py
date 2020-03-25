from .human import Human

class Player:
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._race = Human()
        self._class = None
        self._objects = None

    def set_race(self, race):
        self._race = race
    
    def win_help(self):
        pass

    @property
    def level(self):
        pass



