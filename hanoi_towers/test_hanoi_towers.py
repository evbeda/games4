import unittest

from hanoi_towers.token import Token
from hanoi_towers.tower import Tower


class TestHanoiTower(unittest.TestCase):

    def setUp(self):
        self.token_1 = Token(1)
        self.token_2 = Token(2)
    
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

    # def test_tower_push_token_to_empty_tower(self):
    #     tower = Tower()
    #     tower.push_token(self.token_1)
    #     self.assertEqual(len(tower.tokens), 1)