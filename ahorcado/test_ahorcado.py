import unittest
from Ahorcado import Ahorcado

class TestAhorcado(unittest.TestCase):

    def setUp(self):
        self.game = Ahorcado()
        #self.game.getword()

    def test_force_win(self):
        word = self.game.get_word()
        setted_word = set(word)
        for letter in setted_word:
            self.game.play(letter)
        self.assertTrue(self.game.is_win)


if __name__ == "__main__":

    unittest.main()