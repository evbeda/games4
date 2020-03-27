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
from .love_letter_game import LoveLetterGame, TargetMyselfException
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
        self.human_player = self.game.players[0]
        self.pc_player = self.game.players[1]

    def test_player_name_empty(self):
        name = self.human_player.name = None
        self.assertTrue(name is None)

    def test_player_score_0(self):
        score = self.human_player.score
        self.assertEqual(score, 0)

    def test_player_has_1_card(self):
        cards = self.human_player.cards
        self.assertEqual(len(cards), 1)

    def test_player_piece_of_heart_empty(self):
        hearts = self.human_player.hearts
        self.assertEqual(hearts, 0)

    def test_human_player_name(self):
        name = self.human_player.name
        self.assertEqual(name, "Human Player")

    def test_pc_player_name(self):
        name = self.pc_player.name
        self.assertEqual(name, "PC Player")

    def test_player_is_active(self):
        self.assertTrue(self.human_player.is_active)

    def test_player_set_a_card(self):
        self.human_player.draw_card(Card())
        self.assertEqual(len(self.human_player.cards), 2)

    def test_str_human(self):
        text = self.human_player.__str__()
        self.assertEqual(text, "Player: Human Player,"\
                                " Hearts: 0")

    def test_str_pc(self):
        text = self.pc_player.__str__()
        self.assertEqual(text, "Player: PC Player,"\
                                " Hearts: 0")

    def test_discard_card_removes_1_card_from_hand(self):
        previous_length = len(self.human_player.cards)
        self.human_player.discard_card(self.human_player.cards[0])
        self.assertEqual(len(self.human_player.cards), previous_length-1)

    def test_discard_card_adds_score_to_player(self):
        score = self.human_player.cards[0].score
        self.human_player.discard_card(self.human_player.cards[0])
        self.assertEqual(self.human_player.score, score)

    def test_end_of_round_player(self):
        self.human_player.end_of_round()
        discarded_cards = []
        score = 0
        cards = []
        attributes = [discarded_cards, score, cards]
        player_attributes = [self.human_player.discarded, self.human_player.score, self.human_player.cards]
        self.assertEqual(attributes, player_attributes)

    def test_show_card(self):
        card_to_show = self.human_player.cards[0]
        result = self.human_player.show_card()
        self.assertEqual(card_to_show, result)

    def test_end_of_round_cleans_player(self):
        self.human_player.end_of_round()
        self.assertEqual(self.human_player.score, 0)
        self.assertEqual(len(self.human_player.cards), 0)
        self.assertEqual(len(self.human_player.discarded), 0)
        self.assertTrue(self.human_player.is_active)


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Priest()
        self.genericCard = Card()
        self.game = LoveLetterGame("me")
        self.king = King()
        self.player_1 = self.game.players[0]
        self.player_1.cards.append(self.king)
        self.king.player = self.player_1
        self.player_1.discarded.append(Guard())
        self.player_2 = self.game.players[1]
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
        card_to_draw = Guard()
        self.player_1.draw_card(card_to_draw)
        self.assertEqual(card_to_draw.player, self.player_1)


    def test_end_of_round_sets_player_to_none(self):
        self.king.player.end_of_round()
        self.assertEqual(self.king.player, None)



class TestPrincess(unittest.TestCase):

    def setUp(self):
        self.princess = Princess()
        self.game = LoveLetterGame("me")
        self.player = self.game.players[0]

    def test_execute_action_knocks_out_player(self):
        self.princess.execute_action(self.player)
        self.assertFalse(self.player.is_active)


class TestCountess(unittest.TestCase):

    def setUp(self):
        self.countess = Countess()
        self.game = LoveLetterGame("me")
        self.player = self.game.players[0]
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
        self.player_1 = self.game.players[0]
        self.player_1.cards.append(Countess())
        self.player_2 = self.game.players[1]
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
        self.player_1 = self.game.players[0]
        self.player_1.cards = []
        self.player_1.cards.append(self.countess)
        self.baron.player = self.player_1

        self.player_2 = self.game.players[1]
        self.player_2.cards = []
        self.player_2.cards.append(self.guard)

    def test_compare_hands_and_knock_out_opponent(self):
        self.baron.player = self.player_1
        self.baron.execute_action(self.player_2)
        self.assertFalse(self.player_2.is_active)

    def test_compare_hands_and_knock_out_himself(self):
        self.baron.player = self.player_2
        self.baron.execute_action(self.player_1)
        self.assertFalse(self.player_2.is_active)

    def test_compare_hands_and_tie(self):
        self.guard2 = Guard()
        self.player_1.cards[0] = self.guard2
        self.player_2.cards[0] = self.guard
        self.guard2.player = self.player_1
        self.guard.player = self.player_2
        self.baron.execute_action(self.player_2)
        self.assertTrue(self.player_1.is_active)
        self.assertTrue(self.player_2.is_active)


class TestPriest(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.priest = Priest()
        self.card_1 = King()
        self.player_2.cards.append(self.card_1)

    def test_execute_action(self):
        text_to_show = self.card_1.__str__()
        result = self.priest.execute_action(self.player_2)
        self.assertEqual(text_to_show, result)


class TestPrince(unittest.TestCase):

    def setUp(self):
        self.prince = Prince()
        self.guard = Guard()
        self.priest = Priest()
        self.princess = Princess()
        self.game = LoveLetterGame("me")
        self.player_1 = self.game.players[0]
        self.player_1.cards[0] = self.guard
        self.player_2 = self.game.players[1]
        self.player_2.cards[0] = self.priest
        self.prince.player = self.player_1

    def test_prince_action_on_enemy(self):
        self.prince.execute_action(self.player_2)
        self.assertIsNot(self.player_2.cards[0], self.priest)
        self.assertEqual(len(self.player_1.cards), 1)
    
    def test_prince_action_on_self(self):
        self.prince.execute_action(self.player_1)
        self.assertIsNot(self.player_1.cards[0], self.guard)

    def test_prince_action_on_princess(self):
        self.player_2.cards[0] = self.princess
        self.prince.execute_action(self.player_2)
        self.assertIsNot(self.player_2.cards[0], self.princess)
        self.assertEqual(len(self.player_1.cards), 1)
        self.assertFalse(self.player_2.is_active)


class TestLoveLetterGame(unittest.TestCase):

    def setUp(self):
        self.game = LoveLetterGame("Me")

    def test_player_exsistence_when_init(self):
        number_of_players = 2
        result = len(self.game.players)
        self.assertEquals(number_of_players, result)

    def test_board_with_initial_situation(self):
        expected_text = "Deck : 10 remaining cards\n"\
                        "Player: Me, Hearts: 0\n"\
                        "Player: PC Player, Hearts: 0"
        result_text = self.game.board
        self.assertEquals(expected_text, result_text)

    def test_check_winner_false(self):
        self.assertFalse(self.game.check_winner())

    def test_check_winner_true(self):
        self.game.players[1].hearts = 7
        self.assertTrue(self.game.check_winner())

    def test_end_of_round(self):
        for player in self.game.players:
            player.end_of_round()
        discarded_cards = []
        score = 0
        cards = []
        attributes = [discarded_cards, score, cards]
        player_attributes = [self.game.players[0].discarded,
                             self.game.players[0].score,
                             self.game.players[0].cards]
        pc_player_attributes = [self.game.players[1].discarded,
                                self.game.players[1].score,
                                self.game.players[1].cards]

        self.assertEqual(attributes, player_attributes)
        self.assertEqual(attributes, pc_player_attributes)

    def test_get_opponents(self):
        opponents = self.game.players.copy()
        opponents.remove(self.game.current_player)
        result = self.game.get_opponents()
        self.assertEquals(opponents, result)

    def test_select_target_enemy(self):
        target = self.game.players[1]
        result = self.game.select_target(self.game.players[1].name)
        self.assertEquals(target, result)

    def test_select_target_current_player(self):
        with self.assertRaises(TargetMyselfException):
            result = self.game.select_target(self.game.players[0].name)
