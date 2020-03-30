import unittest

from ur_game.token import Token


class TestUr(unittest.TestCase):

    def test_token(self):
        token = Token()
        self.assertEqual(token.player, None)