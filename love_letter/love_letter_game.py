from love_letter.deck import Deck
from love_letter.human_player import HumanPlayer
from love_letter.pc_player import PcPlayer


class LoveLetterGame:

    def __init__(self, name):
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.human_player = HumanPlayer(name, deck=self.deck)
        self.pc_player = PcPlayer(deck=self.deck)
        self.players = [self.human_player, self.pc_player]
        self.deck.remove_last()
        cards_to_show = self.deck.show_three()
        #move this print to method next turn(only first turn)
        for card in cards_to_show:
            pass

    def next_turn(self):
       return #-> lo que le debemos mostrar al usuario en su turno actual

    def play(self, number):
       #lo que ingreso el usuario por input (puede ser mas de un valor)
       return #-> el resultado de lo que ingreso el usuario: ejemplo: You Win

    @property
    def board(self):
        text_to_show = "{}\n{}\n{}".format(self.deck.__str__(), self.human_player.__str__(), self.pc_player.__str__())
        return text_to_show #-> muestra al usuario el estado actual del juego (no del feedback de lo que acaba de hacer)

    def end_of_round(self):
        self.human_player.end_of_round()
        self.pc_player.end_of_round()

    def check_winner(self):
        if self.human_player.hearts == 7 or self.pc_player.hearts == 7:
            return True
        else:
            return False