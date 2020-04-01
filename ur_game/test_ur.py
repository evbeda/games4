import unittest

from ur_game.cell import Cell
from ur_game.player import Player
from ur_game.token import Token
from ur_game.ur import UrGame


class TestUr(unittest.TestCase):

    def test_token(self):
        token = Token()
        self.assertEqual(token.player, None)

    def test_player(self):
        player = Player()
        self.assertEqual(len(player.initial), 7)
        self.assertEqual(len(player.final_stack), 0)

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

    def test_game(self):
        ur = UrGame()
        self.assertEqual(len(ur.players), 2)
        self.assertEqual(ur.players[0].shared, ur.players[1].shared)

    def test_player_finish(self):
        player = Player()
        self.assertEqual(len(player.finish), 2)

