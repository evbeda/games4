import unittest

from hanoi_towers.token import Token


class TestHanoiTower(unittest.TestCase):

    def test_token_basic_info(self):
        token = Token(5)
        self.assertEqual(token.size, 5)
