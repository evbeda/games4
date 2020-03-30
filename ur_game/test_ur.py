import unittest

from ur_game.cell import Cell
from ur_game.player import Player
from ur_game.token import Token


class TestUr(unittest.TestCase):

    def test_token(self):
        token = Token()
        self.assertEqual(token.player, None)

    def test_player(self):
        player = Player()
        self.assertEqual(len(player.initial), 7)

    def test_cell_empty(self):
        cell = Cell()
        self.assertEqual(cell.token, None)
        self.assertTrue(cell.is_empty)

    def test_cell_full(self):
        cell = Cell()
        cell.token = Token()
        self.assertFalse(cell.is_empty)

    def test_player_start(self):
        player = Player()
        self.assertEqual(len(player.start), 4)

    def test_player_shared(self):
        shared = [Cell() for _ in range(8)]
        player = Player(shared)
        self.assertEqual(len(player.shared), 8)
