import unittest

from hanoi_towers.token import Token
from hanoi_towers.tower import Tower


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