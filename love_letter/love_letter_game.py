from love_letter.card import Card
from love_letter.Cards.baron import Baron


class LoveLetterGame:


    def __init__(self):
        self.cards = self.initDeck(self)


    def next_turn(self):
       return #-> lo que le debemos mostrar al usuario en su turno actual

    def play(self, number):
       #lo que ingreso el usuario por input (puede ser mas de un valor)
       return #-> el resultado de lo que ingreso el usuario: ejemplo: You Win
    @property
    def board(self):
       return #-> muestra al usuario el estado actual del juego (no del feedback de lo que acaba de hacer)

    def initDeck(self):
        pass