import unittest
from Ahorcado import Ahorcado


class TestAhorcado(unittest.TestCase):

    def setUp(self):
        self.game = Ahorcado()
        self.game.word = "PALABRA"

    def test_force_win(self):
        for letter in "PALABRA":
            self.game.play(letter)
        self.assertTrue(self.game.is_win)

    def test_next_turn_win(self):
        for letter in "PALABRA":
            self.game.play(letter)
        my_str = self.game.next_turn()
        self.assertEqual(my_str, "The player already won")

    def test_wrong_letter(self):
        self.game.play("Z")
        self.assertEqual(self.game.lifes, 5)
        my_board = "Wrong letter, you lose one life\n_ _ _ _ _ _ _\nZ \nLifes: 5"
        self.assertEqual(self.game.board, my_board)

    def test_right_letter_p(self):
        self.game.play('P')
        self.assertEqual(self.game.lifes, 6)
        my_board = "Correct letter! Choose another\nP _ _ _ _ _ _\nP \nLifes: 6"
        self.assertEqual(self.game.board, my_board)

    def test_show_board(self):
        my_board = "Welcome to the game! Please choose one letter\n_ _ _ _ _ _ _\n\nLifes: 6"
        self.assertEqual(self.game.board, my_board)

    def test_set_hiden_leters(self):
        self.game.set_hidden_letters('P')
        self.assertEqual(self.game.hidden_letters_message, "P _ _ _ _ _ _")


if __name__ == "__main__":

    unittest.main()