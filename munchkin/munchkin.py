from .player import Player

class Munchkin(object):
    def __init__(self):
        self.__players = []
        #self.tresure_deck = TreasureDeck()
        #self.monster_deck = MonsterDeck()
        self.__current_cards_played = ["card1", "card2"]
        self.player1 = Player("name")

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
        return self.__current_cards_played

    @current_cards_played.setter
    def current_cards_played(self, value):
        self.__current_cards_played.append(value)