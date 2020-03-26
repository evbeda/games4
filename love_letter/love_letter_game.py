from love_letter.deck import Deck
from love_letter.human_player import HumanPlayer
from love_letter.pc_player import PcPlayer


class LoveLetterGame:

    def __init__(self, name):
        self.human_player = HumanPlayer(name)
        self.pc_player = PcPlayer()
        self.players = [self.human_player, self.pc_player]
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.deck.remove_last()
        cards_to_show = self.deck.show_three()
        #move this print to method next turn(only first turn)
        for card in cards_to_show:
            pass
        self.human_player.set_a_card(self.deck.get_one_card())
        self.pc_player.set_a_card(self.deck.get_one_card())

    def next_turn(self):
       return #-> lo que le debemos mostrar al usuario en su turno actual

    def play(self, number):
       #lo que ingreso el usuario por input (puede ser mas de un valor)
       return #-> el resultado de lo que ingreso el usuario: ejemplo: You Win

    @property
    def board(self):
        text_to_show = "{}\n{}\n{}".format(self.deck.__str__(), self.human_player.__str__(), self.pc_player.__str__())
        return text_to_show #-> muestra al usuario el estado actual del juego (no del feedback de lo que acaba de hacer)
