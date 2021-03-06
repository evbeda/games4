import random

from munchkin.treasures import TREASURE_CARDS
from munchkin.treasures.accessories import Accessories
from munchkin.treasures.footwear import Footwear
from munchkin.treasures.headwear import Headwear
from munchkin.treasures.treasure_single_use import TreasureSingleUse
from munchkin.treasures.various import Various
from munchkin.treasures.weapon import Weapon
from munchkin.treasures.armor import Armor
from munchkin.doors import DOOR_CARDS
from munchkin.doors.monster import Monster


class Deck:

    def __init__(self):
        self._cards = []
        self.discard_cards = []

    @property
    def cards(self):
        return self._cards

    def add_discard(self, card_to_add):
        self.discard_cards.append(card_to_add)

    def add_cards(self, cards_to_add):
        self._cards.extend(cards_to_add)

    def shuffle_deck(self):
        random.shuffle(self._cards)

    def reset_cards(self):
        self._cards = self.discard_cards
        self.discard_cards = []
        self.shuffle_deck()

    def draw_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


class DoorDeck(Deck):

    def __init__(self):
        super().__init__()
        card = []
        for monster in DOOR_CARDS['monster']:
            card.append(Monster(**monster))
        self.add_cards(card)


class TreasureDeck(Deck):

    def __init__(self):
        super().__init__()
        card = []
        for arm_card_config in TREASURE_CARDS['weapons']:
            card.append(Weapon(**arm_card_config))
        for armor_card_config in TREASURE_CARDS['armor']:
            card.append(Armor(**armor_card_config))
        for armor_card_config in TREASURE_CARDS['various']:
            card.append(Various(**armor_card_config))
        for armor_card_config in TREASURE_CARDS['headwear']:
            card.append(Headwear(**armor_card_config))
        for armor_card_config in TREASURE_CARDS['accessories']:
            card.append(Accessories(**armor_card_config))
        for armor_card_config in TREASURE_CARDS['footwear']:
            card.append(Footwear(**armor_card_config))
        for armor_card_config in TREASURE_CARDS['single_use']:
            card.append(TreasureSingleUse(**armor_card_config))
        self.add_cards(card)


