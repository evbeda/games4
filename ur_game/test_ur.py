import unittest

from ur_game.cell import Cell
from ur_game.player import Player
from ur_game.player import OccupedCellException, InvalidMovementException, OutOfBoardException
from ur_game.token import Token
from ur_game.ur import UrGame


class TestUr(unittest.TestCase):

    def setUp(self):
        self.game = UrGame()

    def test_token(self):
        token = Token()
        self.assertEqual(token.player, None)

    def test_token_index(self):
        token = Token(1)
        self.assertEqual(token.index, 1)

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

    def test_ur_game_playing(self):
        self.assertTrue(self.game.is_playing)

    def test_ur_game_finished(self):
        player = self.game.players[0]
        for index_token in range(len(player.initial)):
            token = player.initial.pop()
            player.final_stack.append(token)
        self.assertFalse(self.game.is_playing)

    def test_roll_dices(self):
        dice_throw_value = self.game.roll_dices()
        self.assertTrue(dice_throw_value >= 0)
        self.assertTrue(dice_throw_value <= 4)
        self.assertFalse(dice_throw_value > 4)
        self.assertFalse(dice_throw_value < 0)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.game = UrGame()
        self.player = self.game.players[0]
        self.cell = self.player.shared[1]

    def test_get_cell_by_index(self):
        result = self.player.get_cell_by_index(6)
        self.assertEqual(result, self.cell)

    def test_get_cell_by_index_out_of_board(self):
        with self.assertRaises(OutOfBoardException):
            self.player.get_cell_by_index(20)

    def test_special_cell_in_shared_true(self):
        result = self.game.players[0].get_cell_by_index(8)
        self.assertTrue(result.is_special)

    def test_special_cell_in_shared_false(self):
        result = self.game.players[0].get_cell_by_index(7)
        self.assertFalse(result.is_special)

