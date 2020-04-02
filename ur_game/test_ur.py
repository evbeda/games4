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

    def test_search_token_true(self):
        player = self.game.players[0]
        token = player.initial[0]
        search_result = player.search_token(0)
        token_index = search_result[0]
        array_token = search_result[1]
        self.assertEqual(array_token[token_index], token)

    def test_search_token_true2(self):
        '''Se mueve un token para ver si lo sigue buscando bien'''
        player = self.game.players[0]
        first_token = player.initial.pop(0)
        player.shared[0].token = first_token
        search_result = player.search_token(0)
        token_index, array_token = search_result[0], search_result[1]
        self.assertEqual(array_token[token_index].token, first_token)

    def test_search_token_false(self):
        player = self.game.players[0]
        search_result = player.search_token(8)
        self.assertIsNone(search_result)

    def test_player_move_token(self):
        dice = 2
        token_selected = 0
        self.game.players[0].move_token(dice, token_selected)
        self.assertEqual(len(self.game.players[0].initial), 6)
        self.assertFalse(self.game.players[0].start[1].is_empty)
        self.assertEqual(self.game.players[0], self.game.players[0].start[1].token.player)

    def test_player_move_token_start_to_start(self):
        self.game.players[0].move_token(1, 1)
        self.game.players[0].move_token(2, 1)
        self.assertFalse(self.game.players[0].start[2].is_empty)
        self.assertEqual(self.game.players[0].start[2].token.index, 1)

    def test_player_move_token_to_shared(self):
        self.game.players[0].move_token(3, 0)
        self.game.players[0].move_token(2, 0)
        self.assertTrue(self.game.players[0].start[2].is_empty)
        self.assertFalse(self.game.players[0].shared[0].is_empty)
        self.assertEqual(self.game.players[0].shared[0].token.index, 0)

    def test_player_move_token_shared_to_shared(self):
        self.game.players[0].move_token(3, 0)
        self.game.players[0].move_token(2, 0)
        self.game.players[0].move_token(3, 0)
        self.assertFalse(self.game.players[0].shared[3].is_empty)
        self.assertEqual(self.game.players[0].shared[3].token.index, 0)

    def test_player_move_token_to_finish(self):
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(2, 0)
        self.game.players[0].move_token(3, 0)
        self.assertFalse(self.game.players[0].finish[0].is_empty)
        self.assertEqual(self.game.players[0].finish[0].token.index, 0)

    def test_player_move_token_finish_to_finish(self):
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(1, 0)
        self.game.players[0].move_token(1, 0)
        self.assertTrue(self.game.players[0].finish[0].is_empty)
        self.assertEqual(len(self.game.players[0].final_stack), 1)

    def test_player_move_token_to_finish_stack(self):
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(2, 0)
        self.game.players[0].move_token(4, 0)
        self.assertEqual(len(self.game.players[0].final_stack), 1)
        self.assertEqual(self.game.players[0].final_stack[0].index, 0)

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

    def test_move_token_to_occuped_cell_start(self):
        self.game.players[0].move_token(2, 0)
        with self.assertRaises(OccupedCellException):
            self.game.players[0].move_token(2, 1)

    def test_move_token_to_occuped_cell_start_to_share(self):
        self.game.players[0].move_token(3, 0)
        self.game.players[0].move_token(2, 0)
        self.game.players[0].move_token(3, 1)
        with self.assertRaises(OccupedCellException):
            self.game.players[0].move_token(2, 1)

    def test_move_token_to_occuped_cell_share_to_finish(self):
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(4, 0)
        self.game.players[0].move_token(2, 0)
        self.game.players[0].move_token(3, 0)
        self.game.players[0].move_token(4, 1)
        self.game.players[0].move_token(4, 1)
        self.game.players[0].move_token(2, 1)
        with self.assertRaises(OccupedCellException):
            self.game.players[0].move_token(3, 1)


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

    def test_validate_movement_from_empty_cell(self):
        with self.assertRaises(InvalidMovementException):
            self.player.validate_movement(2, 3)

    def test_validate_movement_out_of_board(self):
        with self.assertRaises(InvalidMovementException):
            self.player.validate_movement(0, 3)

    def test_validate_movement_to_own_cell(self):
        self.player.start[1].put_token(self.player.initial[0])
        self.player.start[2].put_token(self.player.initial[1])
        with self.assertRaises(InvalidMovementException):
            self.player.validate_movement(2, 3)

    def test_validate_movement_pass(self):
        self.player.start[1].put_token(self.player.initial[0])
        self.assertTrue(self.player.validate_movement(2, 5))
