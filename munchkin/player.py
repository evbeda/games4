class Player:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.__on_hand = []
        self.__on_board = []
        self.max_race_cards = 1
        self.max_class_cards = 1
        self.max_cards_on_hand = 5
        # La suma de esta variable con el valor del dado
        # debe dar mayor que 0 para poder huir
        self.fleeing_chance = -4

    def set_default_status(self):
        self.max_cards_on_hand = 5
        self.max_race_cards = 1
        self.max_class_cards = 1
        self.fleeing_chance = -4

    def level_up(self):  # Suma mas 1 al nivel
        self.level += 1

    def level_down(self):  # Resta 1 nivel, solo si es mayor a 1
        if self.level > 1:
            self.level -= 1

    def win(self):
        pass  # Gana si el nivel es 10

    def __str__(self):
        card_to_print = ""
        for card in self.__on_hand:
            card_to_print += card.__str__()
        return "Player: {} \n " \
               "On Hand: {}".format(self.name, card_to_print)

    @property
    def on_board(self):
        return self.__on_board

    @on_board.setter
    def on_board(self, on_board):
        self.__on_board = on_board

    @property
    def on_hand(self):
        return self.__on_hand

    @on_hand.setter
    def on_hand(self, on_hand):
        self.__on_hand = on_hand

    def draw_card(self, card):
        try:
            self.validate_max_card()
        except MaxCardsOnHandOutRangeException as e:
            return str(e)
        self.__on_hand.append(card)

    def validate_max_card(self):
        if len(self.__on_hand) + 1 <= self.max_cards_on_hand:
            return True
        else:
            raise MaxCardsOnHandOutRangeException(
                "You have {} on hand, and the maximum number of cards that you can have is {}".format(
                    len(self.__on_hand),
                    self.max_cards_on_hand,
                )
            )


class MaxCardsOnHandOutRangeException(Exception):
    pass
