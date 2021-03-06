from munchkin.deck import DoorDeck, TreasureDeck
from munchkin.player import Player
import random as random


class Munchkin(object):

    def __init__(self):
        self.__players = [Player('1'), Player('2')]
        self.door_deck = DoorDeck()
        self.door_deck.shuffle_deck()
        self.treasure_deck = TreasureDeck()
        self.treasure_deck.shuffle_deck()
        # Reparto de cartas
        for player in self.players:
            for index in range(2):
                treasure_to_draw = self.treasure_deck.draw_card()
                door_to_draw = self.door_deck.draw_card()
                player.draw_card(treasure_to_draw)
                player.draw_card(door_to_draw)
        self.current_player = self.__players[0]
        self.current_card = None

    def next_turn(self):
        response = 'Is your turn: ' + self.current_player.name + '\n'
        return response + 'Card: ' + self.current_card.__str__()

    def play(self, action=None):
        if (type(self.current_card).__name__, "Monster"):
            if not self.current_card.monster_defeated(
                self.current_player,
                self.treasure_deck
            ):
                dice = self.shuffle()
                if (dice + self.current_player.fleeing_chance) < 0:
                    self.current_card.execute_bad_effect()
                    return "You're lose"
                else:
                    return "You're safe"
            else:
                return "You defetead the monster"

    @property
    def board(self):
        board = ''
        for player in self.players:
            board += "Name: {}\n"\
                "Cards on Board:\n".format(player.name)
            for card in player.on_board:
                board += "{}\n".format(card.__str__())
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

    @staticmethod
    def shuffle():
        return random.randint(1, 6)
