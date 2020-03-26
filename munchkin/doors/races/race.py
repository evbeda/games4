from munchkin.doors.door import Door


class Race(Door):

    def __init__(self):

        self._max_cards = 5
        self._carry_objects = False  #boolean

    @property
    def max_cards(self):
        return self._max_cards

    @property
    def carry_objects(self):
        return self._carry_objects

    @max_cards.setter
    def max_cards(self, max_cards):
        self._max_cards = max_cards

    @carry_objects.setter
    def carry_objects(self, carry_objects):
        self._carry_objects = carry_objects
