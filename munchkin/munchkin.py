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
        board = ''
        for player in self.players:
            board += "Name: {}, \n"\
                "Cards on Board:\n".format(player.name)
            for card in player.on_board:
                board += "  {}\n".format(card)
        return board

    @property
    def players(self):
        return self.__players

    def get_current_player(self):
        return self.current_player

    def draw_card(self):
        card = self.door_deck.draw_card()
        current_player = self.get_current_player()
        current_player.draw_card(card)
