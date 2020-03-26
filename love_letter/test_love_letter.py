import unittest

from .card import Card
from .cards.priest import Priest
from .cards.princess import Princess
from .cards.countess import Countess
from .cards.king import King
from .cards.baron import Baron
from .cards.guard import Guard
from .cards.handmaid import Handmaid
from .human_player import HumanPlayer
from .love_letter_game import LoveLetterGame
from .pc_player import PcPlayer
from .player import Player
from .deck import Deck


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_init_deck_with_16_cards(self):
        self.assertEqual(len(self.deck.cards), 16)

    def test_init_five_guards(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Guard":
                result += 1
        self.assertEqual(result, 5)

    def test_init_two_priets(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Priest":
                result += 1
        self.assertEqual(result, 2)

    def test_init_two_baron(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Baron":
                result += 1
        self.assertEqual(result, 2)

    def test_init_two_handmaid(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Handmaid":
                result += 1
        self.assertEqual(result, 2)

    def test_init_two_prince(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Prince":
                result += 1
        self.assertEqual(result, 2)

    def test_init_one_king(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "King":
                result += 1
        self.assertEqual(result, 1)

    def test_init_one_countess(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Countess":
                result += 1
        self.assertEqual(result, 1)

    def test_init_one_princess(self):
        result = 0
        for card in self.deck.cards:
            if card.name == "Princess":
                result += 1
        self.assertEqual(result, 1)

    def test_shuffle_cards(self):
        original_deck = self.deck.cards.copy()
        self.assertNotEqual(original_deck, self.deck.shuffle_cards())

    def test_remove_one(self):
        self.assertEqual(15, len(self.deck.remove_last()))

    def test_show_cards(self):
        self.assertEqual(3, len(self.deck.show_three()))

    def test_len_after_all_discarted(self):
        self.deck.remove_last()
        self.deck.show_three()
        self.assertEqual(12,len(self.deck.cards))

    def test_get_one_card(self):
        card = self.deck.get_one_card()
        self.assertEqual(card.__class__.__name__,"Guard")

    def test_str(self):
        text = self.deck.__str__()
        self.assertEqual("Deck : 16 remaining cards", text)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.human = HumanPlayer("Human Player")

        self.pc_player = PcPlayer()
        self.deck = Deck()
        
        self.player.set_a_card(self.deck.get_one_card())
        self.pc_player.set_a_card(self.deck.get_one_card())

    def test_player_name_empty(self):
        name = self.player.name
        self.assertTrue(name is None)

    def test_player_score_0(self):
        score = self.player.score
        self.assertEqual(score, 0)

    def test_player_has_1_card(self):
        cards = self.player.cards
        self.assertEquals(len(cards), 1)

    def test_player_piece_of_heart_empty(self):
        hearts = self.player.hearts
        self.assertEquals(hearts,0)

    def test_human_player_name(self):
        name = self.human.name
        self.assertEqual(name, "Human Player")

    def test_pc_player_name(self):
        name = self.pc_player.name
        self.assertEqual(name, "PC Player")

    def test_player_is_active(self):
        self.assertTrue(self.player.is_active)

    def test_player_set_a_card(self):
        self.player.set_a_card(self.deck.get_one_card())
        self.assertEqual(len(self.player.cards), 2)

    def test_str_human(self):
        text = self.human.__str__()
        self.assertEquals(text, "Player: Human Player,"\
               " Hearts: 0")

    def test_str_pc(self):
        text = self.pc_player.__str__()
        self.assertEquals(text, "Player: PC Player,"\
               " Hearts: 0")

    def test_discard_card_removes_1_card_from_hand(self):
        previous_length = len(self.player.cards)
        self.player.discard_card(self.player.cards[0])
        self.assertEquals(len(self.player.cards), previous_length-1)

    def test_discard_card_adds_score_to_player(self):
        score = self.player.cards[0].score
        self.player.discard_card(self.player.cards[0])
        self.assertEquals(self.player.score, score)

    def test_end_of_round_player(self):
        self.player.end_of_round()
        discarded_cards = []
        score = 0
        cards = []
        attributes = [discarded_cards, score, cards]
        player_attributes = [self.player.discarded, self.player.score, self.player.cards]
        self.assertEqual(attributes, player_attributes)

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Priest()
        self.genericCard = Card()

    def test_card_print(self):
        self.assertEqual(
            self.card.__str__(),
            "Name: Priest, " \
            "Strength: 2, " \
            "Description: Player is allowed to see another player's hand."
             )

    def test_generic_exception(self):
        self.assertRaises(Exception, lambda: (self.genericCard.execute_action()))


class TestPrincess(unittest.TestCase):

    def setUp(self):
        self.princess = Princess()
        self.player = Player()

    def test_execute_action_knocks_out_player(self):
        self.princess.execute_action(self.player)
        self.assertFalse(self.player.is_active)


class TestCountess(unittest.TestCase):

    def setUp(self):
        self.countess = Countess()
        self.player = Player()
        self.player.cards.append(self.countess)

    def test_must_discard_card_with_king(self):
        self.player.cards.append(King())
        self.assertTrue(self.countess.must_discard(self.player))

    def test_must_discard_card_without_king(self):
        self.player.cards.append(Baron())
        self.assertFalse(self.countess.must_discard(self.player))


class TestKing(unittest.TestCase):

    def setUp(self):
        self.king = King()
        self.player = Player()
        self.player.cards.append(self.king)

        self.player_1 = Player()
        self.player_1.discarded.append(Guard())
        self.player_2 = Player()
        self.player_2.discarded.append(Handmaid())

        self.deck = Deck()
        self.deck.players.extend([self.player, self.player_1, self.player_2])

    def test_looking_for_handmaid(self):
        self.assertEqual(len(self.king.look_for_handmaid(self.deck.players, self.player)), 1)


class TestLoveLetterGame(unittest.TestCase):

    def setUp(self):
        self.game = LoveLetterGame("Me")

    def test_player_exsistence_when_init(self):

        self.assertTrue(self.game.human_player is not None)
        self.assertTrue(self.game.pc_player is not None)

    def test_board_with_initial_situation(self):
        expected_text = "Deck : 10 remaining cards\n"\
                        "Player: Me, Hearts: 0\n"\
                        "Player: PC Player, Hearts: 0"
        result_text = self.game.board
        self.assertEquals(expected_text, result_text)

    def test_check_winner_false(self):
        self.assertFalse(self.game.check_winner())

    def test_check_winner_true(self):
        self.game.pc_player.hearts = 7
        self.assertTrue(self.game.check_winner())
