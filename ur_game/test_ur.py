import unittest

from ur_game.cell import Cell
from ur_game.player import Player
from ur_game.player import InvalidMovementException, OutOfBoardException, TokenProtectedException
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

    def test_cell_empty(self):
        cell = Cell()
        self.assertEqual(cell.token, None)
        self.assertTrue(cell.is_empty)

    def test_cell_full(self):
        cell = Cell()
        cell.token = Token()
        self.assertFalse(cell.is_empty)

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

    def test_player_basic_info(self):
        player = Player()
        self.assertEqual(len(player.shared), 0)
        self.assertEqual(len(player.initial), 7)
        self.assertEqual(len(player.final_stack), 0)
        self.assertEqual(len(player.start), 4)
        self.assertEqual(len(player.finish), 2)

    def test_player_shared(self):
        shared = [Cell() for _ in range(8)]
        player = Player(shared)
        self.assertEqual(len(player.shared), 8)

    def test_validate_movement_from_empty_cell(self):
        player = Player()
        with self.assertRaises(InvalidMovementException):
            player.validate_movement_from_cell(2)

    def test_validate_movement_from_own_cell(self):
        player = Player()
        cell = Cell()
        cell.token = Token(player=player)
        player.start[0] = cell
        result = player.validate_movement_from_cell(1)
        self.assertEqual(result, cell)

    def test_validate_movement_from_opponent_cell(self):
        player = Player()
        opponent = Player()
        cell = Cell()
        cell.token = Token(player=opponent)
        player.start[0] = cell
        with self.assertRaises(InvalidMovementException):
            player.validate_movement_from_cell(1)

    def test_validate_movement_from_initial_fails(self):
        player = Player()
        player.initial = []
        with self.assertRaises(InvalidMovementException):
            player.validate_movement_from_initial()

    def test_move_token_from_cell_to_cell(self):
        player = Player()
        from_cell = Cell()
        to_cell = Cell()
        token = Token()
        from_cell.token = token
        player.move_token_from_cell_to_cell(from_cell, to_cell)
        self.assertIsNone(from_cell.token)
        self.assertEqual(to_cell.token, token)

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

    def test_move_token_from_initial(self):
        player = Player()
        token = Token()
        player.initial[-1] = token
        player.move_token(2, 0)
        self.assertEqual(len(player.initial), 6)
        self.assertEqual(token, player.start[1].token)

    def test_move_token_from_cell(self):
        player = Player()
        token = Token(player=player)
        player.start[0].token = token
        player.move_token(2, 1)
        self.assertIsNone(player.start[0].token)

    def test_validate_movement_to_cell_special_cell(self):
        to_index = 8
        to_cell = self.player.validate_movement_to_cell(to_index)
        self.assertEqual(to_cell, self.player.get_cell_by_index(to_index))

    def test_validate_movement_to_cell_exception_1(self):
        token = self.player.initial.pop()
        to_index = 9
        self.player.get_cell_by_index(to_index).put_token(token)
        with self.assertRaises(InvalidMovementException):
            self.player.validate_movement_to_cell(to_index)
    
    def test_validate_movement_to_cell_exception_2(self):
        player2 = self.game.players[1]
        enemy_token = player2.initial.pop()
        to_index = 8
        player2.get_cell_by_index(to_index).put_token(enemy_token)
        with self.assertRaises(TokenProtectedException):
            self.player.validate_movement_to_cell(to_index)


    def test_validate_movement_to_cell(self):
        to_index = 9
        self.assertEqual(self.player.get_cell_by_index(to_index), self.player.validate_movement_to_cell(to_index))

    def test_move_token_to_cell_final(self):
        to_index = 14
        cell = self.player.get_cell_by_index(to_index)
        token = self.player.initial.pop()
        self.player.move_token_to_cell(cell, token)
        self.assertIn(token, self.player.final_stack)

    def test_move_token_eat_enemy(self):
        from_cell = Cell()
        player_2 = self.game.players[1]
        enemy_token = player_2.initial.pop()
        self.cell.token = enemy_token
        my_token = self.player.initial.pop()
        from_cell.token = my_token
        self.assertEqual(len(player_2.initial), 6)
        self.player.move_token_from_cell_to_cell(from_cell, self.cell)
        self.assertEqual(len(player_2.initial), 7)
