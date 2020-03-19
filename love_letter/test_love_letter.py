import unittest
from .deck import Deck


class TestLoveLetter(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()



    def test_init_deck_with_16_cards(self):
        self.assertEqual(len(self.deck.cards), 16)

    # def test_init_five_guards(self):
    #     LoveLetterGame.initDeck()
    #     result = 0
    #     for card in LoveLetterGame.deck:
    #         if card.name == "Guard":
    #             result += 1
    #     self.assertEqual(result,5)
    #
    # def test_init_five_priets(self):
    #     LoveLetterGame.initDeck()
    #     result = 0
    #     for card in LoveLetterGame.deck:
    #         if card.name == "Priest":
    #             result += 1
    #     self.assertEqual(result,2)
    #
    # def test_init_five_baron(self):
    #     LoveLetterGame.initDeck()
    #     result = 0
    #     for card in LoveLetterGame.deck:
    #         if card.name == "Baron":
    #             result += 1
    #     self.assertEqual(result,2)
    #
    # def test_init_five_handmaid(self):
    #     LoveLetterGame.initDeck()
    #     result = 0
    #     for card in LoveLetterGame.deck:
    #         if card.name == "Handmaid":
    #             result += 1
    #     self.assertEqual(result,2)
    #
    # def test_init_five_prince(self):
    #     LoveLetterGame.initDeck()
    #     result = 0
    #     for card in LoveLetterGame.deck:
    #         if card.name == "Prince":
    #             result += 1
    #     self.assertEqual(result,2)
    #
    # def test_init_five_king(self):
    #     LoveLetterGame.initDeck()
    #     result = 0
    #     for card in LoveLetterGame.deck:
    #         if card.name == "King":
    #             result += 1
    #     self.assertEqual(result,1)
    #
    # def test_init_five_countess(self):
    #     LoveLetterGame.initDeck()
    #     result = 0
    #     for card in LoveLetterGame.deck:
    #         if card.name == "Countess":
    #             result += 1
    #     self.assertEqual(result,1)
    #
    #
    # def test_init_five_princess(self):
    #     LoveLetterGame.initDeck()
    #     result = 0
    #     for card in LoveLetterGame.deck:
    #         if card.name == "Princess":
    #             result += 1
    #     self.assertEqual(result,1)