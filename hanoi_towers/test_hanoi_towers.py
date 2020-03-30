import unittest

from hanoi_towers.token import Token
from hanoi_towers.tower import Tower
from hanoi_towers.hanoi_towers import HanoiTowers


class TestHanoiTower(unittest.TestCase):

    def setUp(self):
        self.token_1 = Token(1)
        self.token_4 = Token(4)

    def test_token_basic_info(self):
        token = Token(5)
        self.assertEqual(token.size, 5)

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
        tower.insert_token(self.token_4)
        self.assertEqual(len(tower.tokens), 1)

    def test_remove_token(self):
        tower = Tower(3)
        self.assertEqual(tower.tokens[-1], tower.remove_token())
        self.assertEqual(len(tower.tokens), 2)

    def test_init_game(self):
        hanoi_towers = HanoiTowers(4)
        self.assertEqual(len(hanoi_towers.tower1.tokens), 4)
        self.assertEqual(len(hanoi_towers.tower2.tokens), 0)
        self.assertEqual(len(hanoi_towers.tower3.tokens), 0)

    def test_next_turn_win(self):
        token1 = Token(1)
        token2 = Token(2)
        token3 = Token(3)
        hanoi_towers = HanoiTowers(3)
        hanoi_towers.tower3.insert_token(token3)
        hanoi_towers.tower3.insert_token(token2)
        hanoi_towers.tower3.insert_token(token1)
        self.assertEqual(hanoi_towers.next_turn(), "You won")

    def test_next_turn_still_playing(self):
        hanoi_towers = HanoiTowers(4)
        self.assertEquals(hanoi_towers.next_turn(), "Plase make your move")
