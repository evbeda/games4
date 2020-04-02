import unittest
from unittest.mock import patch, MagicMock

from ahorcado.ahorcado import Ahorcado
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

        class OutputCollector(object):
            def __init__(self, *args, **kwargs):
                self.output_collector = []

            def __call__(self, output):
                self.output_collector.append(output)

        self.output_collector = OutputCollector()

    @patch('game.Game.get_input', return_value='9')
    def test_quit_game(self, mock_input):
        with patch('game.Game.output', side_effect=self.output_collector):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            [],
        )


    def test_game_selection(self):
        self.assertEqual(
            self.game.game_inputs(),
            'Select Game\n'
            '0: Guess Number Game\n'
            '1: Senku\n'
            '2: Ahorcado\n'
            '3: Hanoi Towers\n'
            '9: to quit\n'
        )

    def test_play_guess_number_game(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '0'
                if 'Give me a number from 0 to 100' in console_output:
                    return '50'

        with \
                patch(
                    'game.Game.get_input', side_effect=ControlInputValues()), \
                patch(
                    'game.Game.output', side_effect=self.output_collector), \
                patch(
                    'guess_number_game.guess_number_game.randint',
                    return_value=50):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            ['[]', 'you win', '[50]'],
        )

    def test_play_ahorcado(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '2'
                if 'Please input a letter from A-Z' in console_output:
                    return 'T'

        with \
                patch(
                    'game.Game.get_input', side_effect=ControlInputValues()), \
                patch(
                    'game.Game.output', side_effect=self.output_collector), \
                patch.object(
                    Ahorcado, 'get_word_from_api',return_value='T'
                    ):
            self.game.play()

        self.assertEqual(
            self.output_collector.output_collector,
            ['_\n\nLifes: 6', 'Game Finished', 'T\nT\nLifes: 6'],
        )

    def test_play_senku(self):

        class ControlInputValues(object):
            def __init__(self, game, *args, **kwargs):
                self.game = game
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '1'
                if "Please, make a move" in console_output:
                    game_moves = (
                        "5 3 3 3",
                        "4 5 4 3",
                        "6 4 4 4",
                        "6 2 6 4",
                        "3 4 5 4",
                        "6 4 4 4",
                        "4 3 4 5",
                        "4 6 4 4",
                        "4 1 4 3",
                        "4 3 4 5",
                        "2 6 4 6",
                        "4 6 4 4",
                        "2 5 4 5",
                        "4 5 4 3",
                        "2 2 4 2",
                        "5 2 3 2",
                        "2 1 4 1",
                        "4 0 4 2",
                        "4 3 4 1",
                        "2 0 4 0",
                        "4 0 4 2",
                        "4 2 2 2",
                        "2 3 2 5",
                        "0 4 2 4",
                        "2 5 2 3",
                        "2 3 2 1",
                        "0 3 2 3",
                        "3 3 1 3",
                        "0 2 2 2",
                        "2 1 2 3",
                        "1 3 3 3",
                    )
                    play = game_moves[self.play_count]
                    self.play_count += 1
                    return play

        with \
                patch(
                    'game.Game.get_input', side_effect=ControlInputValues(self.game)), \
                patch(
                    'game.Game.output', side_effect=self.output_collector):
            self.game.play()
        self.assertEqual(
            self.output_collector.output_collector[-1],
            "  0 1 2 3 4 5 6\n"
            " + = = = = = = =\n"
            "0| X X - - - X X\n"
            "1| X X - - - X X\n"
            "2| - - - - - - -\n"
            "3| - - - 0 - - -\n"
            "4| - - - - - - -\n"
            "5| X X - - - X X\n"
            "6| X X - - - X X\n",
        )
        self.assertEqual(
            self.output_collector.output_collector[-2],
            "You won",
        )

    def test_play_hanoi_towers(self):

        class ControlInputValues(object):
            def __init__(self, *args, **kwargs):
                self.played = False
                self.play_count = 0

            def __call__(self, console_output):
                if 'Select Game' in console_output:
                    if self.played:
                        return '9'
                    self.played = True
                    return '3'
                if 'Enter the numbers of source and target towers' in console_output:
                    game_moves = (
                        "0 1",
                        "0 2",
                        "1 2",
                        "0 1",
                        "2 0",
                        "2 1",
                        "0 2",
                        "2 1",
                        "0 2",
                        "1 2",
                        "1 0",
                        "2 0",
                        "1 2",
                        "0 1",
                        "1 2",
                        "0 2",
                        "2 1",
                        "0 2",
                        "1 2",
                    )

                    play = game_moves[self.play_count]
                    self.play_count += 1
                    return play

        with \
                patch(
                    'game.Game.get_input', side_effect=ControlInputValues(self.game)), \
                patch(
                    'game.Game.output', side_effect=self.output_collector):
            self.game.play()
        self.assertEqual(
            self.output_collector.output_collector[-1],
                "                    |                                        |                                      - | -                  \n" \
                "                    |                                        |                                    - - | - -                \n" \
                "                    |                                        |                                  - - - | - - -              \n" \
                "                    |                                        |                                - - - - | - - - -            \n" \
        )
        self.assertEqual(
            self.output_collector.output_collector[-2],
            "You won",
        )


if __name__ == "__main__":
    unittest.main()
