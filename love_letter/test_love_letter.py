import unittest

from .card import Card
from .cards.guard import Guard
from .cards.priest import Priest
from .cards.baron import Baron
from .cards.handmaid import Handmaid
from .cards.prince import Prince
from .cards.king import King
from .cards.countess import Countess
from .cards.princess import Princess
from .human_player import HumanPlayer
from .love_letter_game import LoveLetterGame
from .pc_player import PcPlayer
from .player import Player
from .deck import Deck


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_init_deck_with_12_cards_after_one_upside_down_and_3_discarded(self):
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
        self.assertEqual(12, len(self.deck.cards))

    def test_str(self):
        text = self.deck.__str__()
        self.assertEqual("Deck : 16 remaining cards", text)


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.game = LoveLetterGame("Human Player")
        self.human_player = self.game.human_player
        self.pc_player = self.game.pc_player

    def test_player_name_empty(self):
        name = self.human_player.name = None
        self.assertTrue(name is None)

    def test_player_score_0(self):
        score = self.human_player.score
        self.assertEqual(score, 0)

    def test_player_has_1_card(self):
        cards = self.human_player.cards
        self.assertEquals(len(cards), 1)

    def test_player_piece_of_heart_empty(self):
        hearts = self.human_player.hearts
        self.assertEquals(hearts, 0)

    def test_human_player_name(self):
        name = self.human_player.name
        self.assertEqual(name, "Human Player")

    def test_pc_player_name(self):
        name = self.pc_player.name
        self.assertEqual(name, "PC Player")

    def test_player_is_active(self):
        self.assertTrue(self.human_player.is_active)

    def test_player_set_a_card(self):
        self.human_player.draw_card()
        self.assertEqual(len(self.human_player.cards), 2)

    def test_str_human(self):
        text = self.human_player.__str__()
        self.assertEquals(text, "Player: Human Player,"\
                                " Hearts: 0")

    def test_str_pc(self):
        text = self.pc_player.__str__()
        self.assertEquals(text, "Player: PC Player,"\
                                " Hearts: 0")

    def test_discard_card_removes_1_card_from_hand(self):
        previous_length = len(self.human_player.cards)
        self.human_player.discard_card(self.human_player.cards[0])
        self.assertEquals(len(self.human_player.cards), previous_length-1)

    def test_discard_card_adds_score_to_player(self):
        score = self.human_player.cards[0].score
        self.human_player.discard_card(self.human_player.cards[0])
        self.assertEquals(self.human_player.score, score)

    def test_end_of_round_player(self):
        self.human_player.end_of_round()
        discarded_cards = []
        score = 0
        cards = []
        attributes = [discarded_cards, score, cards]
        player_attributes = [self.human_player.discarded, self.human_player.score, self.human_player.cards]
        self.assertEqual(attributes, player_attributes)


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Priest()
        self.genericCard = Card()
        self.game = LoveLetterGame("me")

        self.player_1 = self.game.human_player
        self.player_1.cards.append(King())
        self.player_1.discarded.append(Guard())
        self.player_2 = self.game.pc_player
        self.player_2.discarded.append(Handmaid())

        self.deck = Deck()
        self.deck.players.extend([self.player_1, self.player_2])

    def test_card_print(self):
        self.assertEqual(
            self.card.__str__(),
            "Name: Priest, " \
            "Strength: 2, " \
            "Description: Player is allowed to see another player's hand."
             )

    def test_generic_exception(self):
        self.assertRaises(Exception, lambda: (self.genericCard.execute_action("player")))

    def test_looking_for_handmaid(self):
        self.assertEqual(len(self.genericCard.look_for_handmaid(self.deck.players, self.player_1)), 1)
        self.assertTrue(self.player_2 in self.genericCard.look_for_handmaid(self.deck.players, self.player_1))
        self.assertFalse(self.player_1 in self.genericCard.look_for_handmaid(self.deck.players, self.player_1))

    def test_card_drawn_has_a_player(self):
        self.player_1.draw_card()
        self.card_to_draw = self.player_1.cards[-1]
        self.assertEqual(self.card_to_draw.player, self.player_1)


class TestPrincess(unittest.TestCase):

    def setUp(self):
        self.princess = Princess()
        self.game = LoveLetterGame("me")
        self.player = self.game.human_player

    def test_execute_action_knocks_out_player(self):
        self.princess.execute_action(self.player)
        self.assertFalse(self.player.is_active)


class TestCountess(unittest.TestCase):

    def setUp(self):
        self.countess = Countess()
        self.game = LoveLetterGame("me")
        self.player = self.game.human_player
        self.player.cards = []
        self.player.cards.append(self.countess)

    def test_must_discard_card_with_king(self):
        self.player.cards.append(King())
        self.assertTrue(self.countess.must_discard(self.player))

    def test_must_discard_card_without_king(self):
        # print(self.player.cards)
        self.player.cards.append(Baron())
        self.assertFalse(self.countess.must_discard(self.player))


class TestKing(unittest.TestCase):

    def setUp(self):
        self.king = King()
        self.game = LoveLetterGame("me")
        self.player_1 = self.game.human_player
        self.player_1.cards.append(Countess())
        self.player_2 = self.game.pc_player
        self.player_2.cards.append(Guard())
        

    def test_switch_cards(self):
        self.king.execute_action(self.player_1, self.player_2)
        self.assertEqual(len(self.player_1.cards), 2)
        self.assertTrue("Countess" in card.name for card in self.player_1.cards)
        self.assertEqual(len(self.player_2.cards), 2)
        self.assertTrue("Guard" in card.name for card in self.player_2.cards)


class TestBaron(unittest.TestCase):

    def setUp(self):
        self.baron = Baron()
        self.countess = Countess()
        self.guard = Guard()
        self.princess = Princess()
        self.deck = Deck()

        self.game = LoveLetterGame("me")
        self.player_1 = self.game.human_player
        self.player_1.cards = []
        self.player_1.cards.append(self.countess)
        
        self.player_2 = self.game.pc_player
        self.player_2.cards = []
        self.player_2.cards.append(self.guard)
        
        self.player_3 = Player(self.deck)
        self.player_3.cards = []
        self.player_3.cards.append(self.princess)
        

    def test_compare_hands_and_knock_out_opponent(self):
        self.baron.execute_action(self.player_1, self.player_2)

        shown_card = self.player_1.show_card(self.player_2)
        viewed_card = self.player_2.show_card(self.player_1)
        self.assertEqual(self.countess, shown_card)
        self.assertEqual(self.guard, viewed_card)

        self.assertFalse(self.player_2.is_active)

    def test_compare_hands_and_knock_out_himself(self):
        self.baron.execute_action(self.player_1, self.player_3)

        shown_card = self.player_1.show_card(self.player_3)
        viewed_card = self.player_3.show_card(self.player_1)
        self.assertEqual(self.countess, shown_card)
        self.assertEqual(self.princess, viewed_card)

        self.assertFalse(self.player_1.is_active)

    def test_compare_hands_and_tie(self):
        self.player_1.cards = []
        self.guard2 = Guard()
        self.player_1.cards.append(self.guard2)

        self.baron.execute_action(self.player_1, self.player_2)

        shown_card = self.player_1.show_card(self.player_2)
        viewed_card = self.player_2.show_card(self.player_1)
        self.assertEqual(self.guard2, shown_card)
        self.assertEqual(self.guard, viewed_card)

        self.assertTrue(self.player_1.is_active)
        self.assertTrue(self.player_2.is_active)

    
class TestPrince(unittest.TestCase):

    def setUp(self):
        self.prince = Prince()
        self.guard = Guard()
        self.priest = Priest()
        self.princess = Princess()
        self.game = LoveLetterGame("me")
        self.player_1 = self.game.human_player
        self.player_1.cards[0] = self.guard
        self.player_2 = self.game.pc_player
        self.player_2.cards[0] = self.priest

    def test_prince_action_on_enemy(self):
        self.prince.execute_action(self.player_1, self.player_2)
        self.assertIsNot(self.player_2.cards[0], self.priest)
        self.assertEqual(len(self.player_1.cards), 1)
    
    def test_prince_action_on_self(self):
        self.prince.execute_action(self.player_1, self.player_1)
        self.assertIsNot(self.player_1.cards[0], self.guard)

    def test_prince_action_on_princess(self):
        self.player_2.cards[0] = self.princess
        self.prince.execute_action(self.player_1, self.player_2)
        self.assertIsNot(self.player_2.cards[0], self.princess)
        self.assertEqual(len(self.player_1.cards), 1)
        self.assertFalse(self.player_2.is_active)

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

    def test_end_of_round(self):
        for player in self.game.players:
            player.end_of_round()
        discarded_cards = []
        score = 0
        cards = []
        attributes = [discarded_cards, score, cards]
        player_attributes = [self.game.human_player.discarded,
                             self.game.human_player.score,
                             self.game.human_player.cards]
        pc_player_attributes = [self.game.pc_player.discarded,
                                self.game.pc_player.score,
                                self.game.pc_player.cards]

        self.assertEqual(attributes, player_attributes)
        self.assertEqual(attributes, pc_player_attributes)

