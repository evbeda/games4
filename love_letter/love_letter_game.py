from love_letter.deck import Deck
from love_letter.human_player import HumanPlayer
from love_letter.pc_player import PcPlayer


class TargetMyselfException(Exception):
    pass




class LoveLetterGame:

    def __init__(self, name):
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.players = [HumanPlayer(name, self), PcPlayer(self)]
        #Logica de sacar cartas (regla del juego para 2 jugadores)
        if len(self.players) == 2:
            self.deck.remove_last()
            self.deck.show_three()

        for player in self.players:
            card = self.deck.draw_card()
            player.draw_card(card)

        self.current_player = self.players[0]



    def next_turn(self):
       return #-> lo que le debemos mostrar al usuario en su turno actual

    def play(self, number):
       #lo que ingreso el usuario por input (puede ser mas de un valor)
       return #-> el resultado de lo que ingreso el usuario: ejemplo: You Win

    @property
    def board(self):
        text_to_show = "{}".format(self.deck.__str__())
        for player in self.players:
            text_to_show+="\n{}".format(player.__str__())
        return text_to_show #-> muestra al usuario el estado actual del juego (no del feedback de lo que acaba de hacer)

    def end_of_round(self):
        self.human_player.end_of_round()
        self.pc_player.end_of_round()

    def check_winner(self):
        if self.human_player.hearts == 7 or self.pc_player.hearts == 7:
            return True
        else:
            return False

    def get_opponents(self):
        players_duplicate = self.players.copy()
        players_duplicate.remove(self.current_player)
        return players_duplicate

    def select_target(self, player_name):
        if player_name == self.current_player.name:
            raise TargetMyselfException()
        for player in self.players:
            if player.name == player_name:
                return player

    def get_deck_card(self):
        return self.deck.draw_card()
