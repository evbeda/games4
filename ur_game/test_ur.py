import unittest

from ur_game.player import Player
from ur_game.token import Token


class TestUr(unittest.TestCase):

    def test_token(self):
        token = Token()
        self.assertEqual(token.player, None)

    def test_player(self):
        player = Player()
        self.assertEqual(len(player.initial), 7)