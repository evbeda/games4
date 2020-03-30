import unittest

from hanoi_towers.token import Token
from hanoi_towers.tower import Tower


class TestHanoiTower(unittest.TestCase):

    def test_token_basic_info(self):
        token = Token(5)
        self.assertEqual(token.size, 5)

    def test_tower_basic_info(self):
        tower = Tower()
        self.assertEqual(len(tower.tokens), 0)
