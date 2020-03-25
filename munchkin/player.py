
class Player:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.onHand = []
        self.onBoard = []
        self.max_race_cards = 1
        self.max_class_cards = 1
        self.max_cards_on_hand = 5
        self.fleeing_chance = -4 # La suma de esta variable con el valor del dado, debe dar mayor que 0 para poder huir
    
    def set_default_status(self):
        self.max_cards_on_hand = 5
        self.max_race_cards = 1
        self.max_class_cards = 1
        self.fleeing_chance = -4
    
    def level_up(self): # Suma mas 1 al nivel
        self.level += 1
    
    def level_down(self): # Resta 1 nivel, solo si es mayor a 1
        if self.level > 1:
            self.level -= 1

    def win(self):
        pass # Gana si el nivel es 10

