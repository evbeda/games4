import unittest

from .Player import Player
from .deck import Deck


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_init_deck_with_16_cards(self):
        self.assertEqual(len(self.deck.cards), 16)

    def test_init_five_guards(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Guard":
                result += 1
        self.assertEqual(result, 5)

    def test_init_two_priets(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Priest":
                result += 1
        self.assertEqual(result, 2)

    def test_init_two_baron(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Baron":
                result += 1
        self.assertEqual(result, 2)

    def test_init_two_handmaid(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Handmaid":
                result += 1
        self.assertEqual(result, 2)

    def test_init_two_prince(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Prince":
                result += 1
        self.assertEqual(result, 2)

    def test_init_one_king(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "King":
                result += 1
        self.assertEqual(result, 1)

    def test_init_one_countess(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Countess":
                result += 1
        self.assertEqual(result, 1)


    def test_init_one_princess(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Princess":
                result += 1
        self.assertEqual(result, 1)

    def test_shuffle_cards(self):
        original_deck = self.deck.cards.copy()
        self.assertNotEqual(original_deck, self.deck.shuffle_cards())

    def test_remove_one(self):
        self.assertEqual(15, len(self.deck.remove_last()))

    def test_show_cards(self):
        self.assertEqual(3, len(self.deck.show_three()))

    def test_len_after_all_discarted(self):
        self.deck.remove_last()
        self.deck.show_three()
        self.assertEqual(12,len(self.deck.cards))

    def test_get_one_card(self):
        card = self.deck.get_one_card()
        self.assertEqual(card.__class__.__name__,"Guard")

class TestPlayer(unittest.TestCase):

    def setUp(self):
       self.player = Player()

    def test_player_name_not_empty(self):
        name = self.player.name
        self.assertTrue(name is not None)

    def test_player_cards_empty(self):
        cards = self.player.cards
        self.assertEquals(cards, [] )

    def test_player_piece_of_heart_empty(self):
        hearts = self.player.hearts
        self.assertEquals(hearts,0)

