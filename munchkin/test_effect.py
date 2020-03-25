import unittest

from board import Board
from effect import DrawCardEffect
from player import Player


class TestEffect(unittest.TestCase):

    def setUp(self):
        Board.current_player = Player("me")
        Board.treasure_deck = [object() for index in range(50)]
        self.get_cards_effect = DrawCardEffect()

    def test_get_cards_successfully(self):
        Board.current_player.cards_on_hand = [object() for index in range(3)]
        cards_before_effect = len(Board.current_player.cards_on_hand)
        self.get_cards_effect.apply_effect(deck=Board.treasure_deck, number_of_cards=1)
        cards_after_effect = len(Board.current_player.cards_on_hand)
        self.assertEqual(cards_before_effect+1, cards_after_effect)


if __name__ == "__main__":
    unittest.main()