import unittest
import unittest.mock
from Ahorcado import Ahorcado


class TestAhorcado(unittest.TestCase):

    def setUp(self):
        self.game = Ahorcado()
        self.game.word = "PALABRA"

    
    def test_next_turn_playing(self):
        self.assertEqual(self.game.next_turn(), "Please input a letter from A-Z")
    
    def test_next_turn_win(self):
        self.game.is_win = True
        self.assertEqual(self.game.next_turn(), "The player already won")
    
    def test_next_turn_lose(self):
        self.game.is_lose = True
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


if __name__ == "__main__":

    unittest.main()