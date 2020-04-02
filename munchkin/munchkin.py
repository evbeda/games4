from munchkin.deck import DoorDeck
from munchkin.player import Player


class Munchkin(object):
    def __init__(self):
        self.__players = [Player('1'), Player('2')]
        self.door_deck = DoorDeck()
        #self.tresure_deck = TreasureDeck()
        self.current_player = self.__players[0]

    # def next_turn(self):
    #     # return -> lo que le debemos mostrar al usuario en su turno actual
    #     pass
    #
    # def play(self, number):
    #     # lo que ingreso el usuario por input (puede ser mas de un valor)
    #     # return -> el resultado de lo que ingreso el usuario: ejemplo: You Win
    #     pass
    #

    @property
    def board(self):
        board= "{}\n{}".format(self.current_cards_played.__str__(), self.player1.__str__())
        return board

    @property
    def players(self):
        return self.__players

    #@players.setter
    #def players(self, value):
        #self.__players.append(value)​

    @property
    def current_cards_played(self):
        current_cards_played = {}
        for player in self.__players:
            current_cards_played[player.name].append(player.on_board)
        return current_cards_played

    @current_cards_played.setter
    def current_cards_played(self, value):
        self.__current_cards_played.append(value)

    def get_current_player(self):
        return self.current_player

    def draw_card(self):
        card = self.door_deck.draw_card()
        current_player = self.get_current_player()
        current_player.draw_card(card)
