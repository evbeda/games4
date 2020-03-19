import unittest
import string
import random
from Ahorcado import Ahorcado

class TestAhorcado(unittest.TestCase):

    def setUp(self):
        self.game = Ahorcado()
        #self.game.getword()

    def test_force_win(self):
        setted_word = set(self.game.word)
        for letter in setted_word:
            self.game.play(letter)
        self.assertTrue(self.game.is_win)

    def test_wrong_letter(self):
        word = self.game.word
        my_letter = random.choice(string.ascii_letters)
        while my_letter in word:
            my_letter = random.choice(string.ascii_letters)
        self.game.play(my_letter)
        self.assertEqual(self.game.lifes, 5)
        self.assertEqual(self.game.status_message, "Wrong letter, you lose one life")


if __name__ == "__main__":

    unittest.main()