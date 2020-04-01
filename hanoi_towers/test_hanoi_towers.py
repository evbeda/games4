import unittest

from .token import Token
from .tower import Tower, InvalidMovement, EmptyTower
from .hanoi_towers import HanoiTowers


class TestHanoiTower(unittest.TestCase):

    def test_init_game(self):
        hanoi_towers = HanoiTowers(4)
        self.assertEqual(len(hanoi_towers.towers[0].tokens), 4)
        self.assertEqual(len(hanoi_towers.towers[1].tokens), 0)
        self.assertEqual(len(hanoi_towers.towers[2].tokens), 0)
        self.assertTrue(hanoi_towers.is_playing)

    def test_next_turn_win(self):
        token1 = Token(1)
        token2 = Token(2)
        token3 = Token(3)
        hanoi_towers = HanoiTowers(3)
        hanoi_towers.towers[2].insert_token(token3)
        hanoi_towers.towers[2].insert_token(token2)
        hanoi_towers.towers[2].insert_token(token1)
        self.assertEqual(hanoi_towers.next_turn(), "You won")
        self.assertFalse(hanoi_towers.is_playing)

    def test_next_turn_still_playing(self):
        hanoi_towers = HanoiTowers(4)
        self.assertEqual(hanoi_towers.next_turn(), "Plase make your move")
        self.assertTrue(hanoi_towers.is_playing)

    def test_play_right_move(self):
        hanoi_towers = HanoiTowers(4)
        hanoi_towers.play(0, 1)
        self.assertEqual(len(hanoi_towers.towers[0].tokens), 3)
        self.assertEqual(len(hanoi_towers.towers[1].tokens), 1)
        self.assertEqual(len(hanoi_towers.towers[2].tokens), 0)

    def test_play_invalid_move(self):
        hanoi_towers = HanoiTowers(4)
        hanoi_towers.play(0, 1)
        self.assertEqual(hanoi_towers.play(0, 1), "Invalid move")

    def test_play_invalid_move_tokens(self):
        hanoi_towers = HanoiTowers(4)
        hanoi_towers.play(0, 1)
        hanoi_towers.play(0, 1)
        self.assertEqual(len(hanoi_towers.towers[0].tokens), 3)
        self.assertEqual(len(hanoi_towers.towers[1].tokens), 1)

    def test_play_empty_tower(self):
        hanoi_towers = HanoiTowers(4)
        self.assertEqual(hanoi_towers.play(1, 2), "Empty tower")

    def test_play_empty_tower_tokens(self):
        hanoi_towers = HanoiTowers(4)
        hanoi_towers.play(1, 2)
        self.assertEqual(len(hanoi_towers.towers[1].tokens), 0)
        self.assertEqual(len(hanoi_towers.towers[2].tokens), 0)

    def test_board_display(self):
        hanoi_towers = HanoiTowers(4)
        expected_board=  "Tower 0:\n"\
                " |-\n"\
                " |--\n"\
                " |---\n"\
                " |----\n"\
                "\n"\
                "Tower 1:\n"\
                " |\n" \
                " |\n" \
                " |\n" \
                " |\n" \
                "\n" \
                "Tower 2:\n" \
                " |\n" \
                " |\n" \
                " |\n" \
                " |\n" \
                "\n"
        self.assertEqual(hanoi_towers.board, expected_board)

    def test_board_display_after_play(self):
        hanoi_towers = HanoiTowers(4)
        hanoi_towers.play(0, 1)
        expected_board = "Tower 0:\n" \
                         " |\n" \
                         " |--\n" \
                         " |---\n" \
                         " |----\n" \
                         "\n" \
                         "Tower 1:\n" \
                         " |\n" \
                         " |\n" \
                         " |\n" \
                         " |-\n" \
                         "\n" \
                         "Tower 2:\n" \
                         " |\n" \
                         " |\n" \
                         " |\n" \
                         " |\n" \
                         "\n"
        self.assertEqual(hanoi_towers.board,expected_board)

class TestToken(unittest.TestCase):

    def test_token_basic_info(self):
        token = Token(5)
        self.assertEqual(token.size, 5)


class TestTower(unittest.TestCase):

    def setUp(self):
        self.token_1 = Token(1)
        self.token_4 = Token(4)

    def test_tower_basic_info(self):
        tower = Tower()
        self.assertEqual(len(tower.tokens), 0)

    def test_tower_with_tokens(self):
        tower = Tower(4)
        self.assertEqual(tower.tokens[0].size, 4)
        self.assertEqual(tower.tokens[1].size, 3)
        self.assertEqual(tower.tokens[2].size, 2)
        self.assertEqual(tower.tokens[3].size, 1)
        self.assertEqual(len(tower.tokens), 4)

    def test_validate_insert_token_empty_tokens(self):
        tower = Tower()
        self.assertTrue(tower.validate_insert_token(self.token_1))

    def test_validate_insert_token_valid_tokens(self):
        tower = Tower()
        tower.tokens.append(self.token_4)
        self.assertTrue(tower.validate_insert_token(self.token_1))

    def test_validate_insert_token_invalid_tokens(self):
        tower = Tower()
        tower.tokens.append(self.token_1)
        self.assertFalse(tower.validate_insert_token(self.token_4))

    def test_tower_insert_token_to_empty_tower(self):
        tower = Tower()
        tower.insert_token(self.token_1)
        self.assertEqual(len(tower.tokens), 1)

    def test_tower_insert_token_to_valid_tower(self):
        tower = Tower()
        tower.tokens.append(Token(3))
        tower.insert_token(self.token_1)
        self.assertEqual(len(tower.tokens), 2)

    def test_tower_insert_token_to_invalid_tower(self):
        tower = Tower()
        tower.tokens.append(Token(2))
        with self.assertRaises(InvalidMovement):
            tower.insert_token(self.token_4)
        self.assertEqual(len(tower.tokens), 1)

    def test_remove_token(self):
        tower = Tower(3)
        self.assertEqual(tower.tokens[-1], tower.remove_token())
        self.assertEqual(len(tower.tokens), 2)

    def test_remove_token_empty_tower(self):
        tower = Tower()
        with self.assertRaises(EmptyTower):
            tower.remove_token()
