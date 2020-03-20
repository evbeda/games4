from love_letter.deck import Deck
from love_letter.human_player import HumanPlayer
from love_letter.pc_player import PcPlayer


class LoveLetterGame:

    def __init__(self, name):
        self.human_player = HumanPlayer(name)
        self.pc_player = PcPlayer()
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.deck.remove_last()
        cards_to_show = self.deck.show_three()
        print("This cards must show to you")
        for card in cards_to_show:
            print(card)
        self.human_player.set_a_card(self.deck.get_one_card())
        self.pc_player.set_a_card(self.deck.get_one_card())

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