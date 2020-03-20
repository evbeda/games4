import unittest

from .card import Card
from .cards.priest import Priest
from .human_player import HumanPlayer
from .love_letter_game import LoveLetterGame
from .pc_player import PcPlayer
from .player import Player
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
       self.human = HumanPlayer("Human Player")
       self.pc_player = PcPlayer()
       self.deck = Deck()

    def test_player_name_empty(self):
        name = self.player.name
        self.assertTrue(name is None)

    def test_player_cards_empty(self):
        cards = self.player.cards
        self.assertEquals(cards, [])

    def test_player_piece_of_heart_empty(self):
        hearts = self.player.hearts
        self.assertEquals(hearts,0)

    def test_human_player_name(self):
        name = self.human.name
        self.assertEqual(name, "Human Player")

    def test_pc_player_name(self):
        name = self.pc_player.name
        self.assertEqual(name, "Ninja in Pijama!")

    def test_play_set_a_card(self):
        self.player.set_a_card(self.deck.get_one_card())
        self.assertEqual(len(self.player.cards), 1)


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Priest()
        self.genericCard = Card()

    def test_card_print(self):
        self.assertEqual(
            self.card.__str__(),
            "Name: Priest  " \
            "Strength: 2 " \
            "Description Player is allowed to see another player's hand."
             )

    def test_generic_exception(self):
        self.assertRaises(Exception, lambda:(self.genericCard.execute_action()))


class TestLoveLetterGame(unittest.TestCase):

    def setUp(self):
        self.game = LoveLetterGame("Me")

    def test_player_exsistence(self):

        self.assertTrue(self.game.human_player is not None)
        self.assertTrue(self.game.pc_player is not None)

