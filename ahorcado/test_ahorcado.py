import unittest
from .ahorcado import Ahorcado, IsNotAlphaException, IsNotOneCharacter
from mock import patch, MagicMock


class TestAhorcado(unittest.TestCase):

    def setUp(self):
        self.game = Ahorcado('PALABRA')

    def test_next_turn_playing(self):
        self.assertEqual(self.game.next_turn(), "Please input a letter from A-Z")

    def test_next_turn_win(self):
        self.game.used_letters = ["P", "A", "L", "B", "R"]
        self.assertEqual(self.game.next_turn(), "The player already won")

    def test_next_turn_lose(self):
        self.game.lifes = 0
        self.assertEqual(self.game.next_turn(), "The player already lost")

    def test_play_correct(self):
        self.assertEqual(self.game.play("P"), "Correct letter! Choose another")

    def test_play_repeat(self):
        self.game.play("P")
        self.assertEqual(self.game.play("P"), "Already tried that Letter! Try again")

    def test_play_wrong(self):
        self.assertEqual(self.game.play("Z"), "Wrong letter, you lose one life")
        self.assertEqual(self.game.lifes, 5)

    def test_get_lifes_changes(self):
        self.assertEqual(self.game.get_lifes(), "Lifes: 6")
        self.game.play("Z")
        self.assertEqual(self.game.get_lifes(), "Lifes: 5")

    def test_get_lifes_no_change_on_correct(self):
        self.assertEqual(self.game.get_lifes(), "Lifes: 6")
        self.game.play("P")
        self.assertEqual(self.game.get_lifes(), "Lifes: 6")

    def test_get_lifes_no_change_on_repeat(self):
        self.assertEqual(self.game.get_lifes(), "Lifes: 6")
        self.game.play("P")
        self.game.play("P")
        self.assertEqual(self.game.get_lifes(), "Lifes: 6")

    def test_hidden_letters_message(self):
        self.assertEqual(self.game.hidden_letters_message(), "_ _ _ _ _ _ _")

    def test_hidden_letters_message_P(self):
        self.game.play("P")
        self.assertEqual(self.game.hidden_letters_message(), "P _ _ _ _ _ _")

    def test_hidden_letters_message_P_A(self):
        self.game.play("P")
        self.game.play("A")
        self.assertEqual(self.game.hidden_letters_message(), "P A _ A _ _ A")

    def test_hidden_letters_message_P_A_A(self):
        self.game.play("P")
        self.game.play("A")
        self.game.play("A")
        self.assertEqual(self.game.hidden_letters_message(), "P A _ A _ _ A")

    def test_hidden_letters_message_P_Z(self):
        self.game.play("P")
        self.game.play("Z")
        self.assertEqual(self.game.hidden_letters_message(), "P _ _ _ _ _ _")

    def test_hidden_letters_message_PALABRA(self):
        self.game.play("P")
        self.game.play("A")
        self.game.play("L")
        self.game.play("B")
        self.game.play("R")
        self.assertEqual(self.game.hidden_letters_message(), "P A L A B R A")

    def test_hidden_letters_message_all_wrong(self):
        self.game.play("Z")
        self.game.play("Q")
        self.game.play("U")
        self.game.play("K")
        self.game.play("V")
        self.assertEqual(self.game.hidden_letters_message(), "_ _ _ _ _ _ _")

    def test_check_input_used_letters_true(self):
        self.game.play("P")
        self.assertTrue(self.game.check_input_used_letters("P"))

    def test_check_input_used_letters_false(self):
        self.game.play("Z")
        self.assertFalse(self.game.check_input_used_letters("P"))

    def test_check_input_word_true(self):
        self.assertTrue(self.game.check_input_word("P"))

    def test_check_input_word_false(self):
        self.assertFalse(self.game.check_input_word("Z"))

    def test_set_used_letters_P(self):
        self.game.set_used_letters("P")
        self.assertTrue("P" in self.game.used_letters)

    def test_set_used_letters_Z(self):
        self.game.set_used_letters("Z")
        self.assertTrue("Z" in self.game.used_letters)

    def test_board_min(self):
        self.assertEqual(self.game.board, "_ _ _ _ _ _ _\n\nLifes: 6")

    def test_board_w_one_letter(self):
        self.game.play("P")
        self.assertEqual(self.game.board, "P _ _ _ _ _ _\nP\nLifes: 6")

    def test_board_w_two_letters(self):
        self.game.play("P")
        self.game.play("A")
        self.assertEqual(self.game.board, "P A _ A _ _ A\nP A\nLifes: 6")

    def test_board_w_three_letters_one_wrong(self):
        self.game.play("P")
        self.game.play("A")
        self.game.play("Z")
        self.game.play("W")
        self.assertEqual(self.game.board, "P A _ A _ _ A\nP A Z W\nLifes: 4")

    @patch(
        'ahorcado.ahorcado.requests.get',
    )
    def test_get_word_from_api_str(self, mock_get):
        response = MagicMock()
        response.json = MagicMock(return_value=["hola"])
        mock_get.return_value = response
        self.assertTrue(isinstance(self.game.get_word_from_api(), str))

    def test_get_word_from_api_upper(self):
        response = MagicMock()
        response.json = MagicMock(return_value=["PALABRA"])
        with patch('ahorcado.ahorcado.requests.get') as mock_get:
            mock_get.return_value = response
        self.assertTrue(self.game.get_word_from_api().isupper())

    def test_get_word_from_api_no_mistakes(self):
        response = MagicMock()
        response.json = MagicMock(return_value=["ALGO"])
        with patch('ahorcado.ahorcado.requests.get') as mock_get:
            mock_get.return_value = response
        self.assertTrue(self.game.get_word_from_api().isalpha())

    def test_no_alpha(self):
        self.assertRaises(IsNotAlphaException, self.game.validate_letter, '[')

    def test_no_one_character(self):
        self.assertRaises(IsNotOneCharacter, self.game.validate_letter, 'asdsda0321')


if __name__ == "__main__":
    unittest.main()
