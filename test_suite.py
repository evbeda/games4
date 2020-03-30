import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from senku.test_senku import TestSenku
from love_letter.test_love_letter import TestDeck, TestPlayer, TestLoveLetterGame, TestCard, TestPrincess\
                                        , TestCountess\
                                        , TestKing, TestPrince, TestBaron, TestGuard

from ahorcado.test_ahorcado import TestAhorcado
from munchkin.test_munchkin import (
    TestDice,
    TestMonster,
    TestPlayer as MunchkinTestPlayer,
    TestRace,
    TestMunchkin,
    TestTreasureDeck,
    TestCardMunchkin,
    TestDoorDeck
)
from hanoi_towers.test_hanoi_towers import TestHanoiTower
from test_game import TestGame
from ur_game.test_ur import TestUr


def suite():
    test_suite = unittest.TestSuite()
    # GUESS NUMBER GAME
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    test_suite.addTest(unittest.makeSuite(TestSenku))
    #Munchkin
    test_suite.addTest(unittest.makeSuite(TestDice))
    test_suite.addTest(unittest.makeSuite(TestMonster))
    test_suite.addTest(unittest.makeSuite(MunchkinTestPlayer))
    test_suite.addTest(unittest.makeSuite(TestRace))
    test_suite.addTest(unittest.makeSuite(TestMunchkin))
    test_suite.addTest(unittest.makeSuite(TestTreasureDeck))
    test_suite.addTest(unittest.makeSuite(TestDoorDeck))
    test_suite.addTest(unittest.makeSuite(TestCardMunchkin))
    #Love Letter Game
    test_suite.addTest(unittest.makeSuite(TestDeck))
    test_suite.addTest(unittest.makeSuite(TestGuard))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    test_suite.addTest(unittest.makeSuite(TestLoveLetterGame))
    test_suite.addTest(unittest.makeSuite(TestCard))
    test_suite.addTest(unittest.makeSuite(TestPrincess))
    test_suite.addTest(unittest.makeSuite(TestCountess))
    test_suite.addTest(unittest.makeSuite(TestKing))
    test_suite.addTest(unittest.makeSuite(TestPrince))
    test_suite.addTest(unittest.makeSuite(TestBaron))
    # Ahorcado game
    test_suite.addTest(unittest.makeSuite(TestAhorcado))
    # Hanoi Towes
    test_suite.addTest(unittest.makeSuite(TestHanoiTower))
    # GAME MACHINE
    test_suite.addTest(unittest.makeSuite(TestGame))
    #Ur Game
    test_suite.addTest(unittest.makeSuite(TestUr))

    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
