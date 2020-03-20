
class Race:

    def __init__(self, name, max_cards, max_objects):
        
        self._name = name
        self._max_cards = max_cards
        self._max_objects = max_objects
   
    @property
    def name(self):
        return self._name

    @property
    def max_cards(self):
        return self._max_cards

    @property
    def max_objects(self):
        return self._max_objects