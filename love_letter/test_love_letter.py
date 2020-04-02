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
from .love_letter_game import LoveLetterGame, TargetMyselfException, TargetInvalidException
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
        self.str_player = Player()

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
        self.str_player.cards.append(Guard())
        text = self.str_player.__str__()
        self.assertEqual(text, "Player: None, Hearts: 0, Cards: 0-Guard ")

    def test_str_pc(self):
        self.pc_player.cards.pop()
        self.pc_player.cards.append(Guard())
        text = self.pc_player.__str__()
        self.assertEqual(text, "Player: PC Player, Hearts: 0, Cards: 0-Guard ")

    def test_discard_card_removes_1_card_from_hand(self):
        previous_length = len(self.human_player.cards)
        self.human_player.discard_card(self.human_player.cards[0])
        self.assertEqual(len(self.human_player.cards), previous_length - 1)

    def test_discard_card_adds_score_to_player(self):
        score = self.human_player.cards[0].score
        self.human_player.discard_card(self.human_player.cards[0])
        self.assertEqual(self.human_player.score, score)

    def test_end_of_round_player(self):
        self.human_player.reset_round()
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
        self.human_player.reset_round()
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
            "Name: Priest, "
            "Strength: 2, "
            "Description: Player is allowed to see another player's hand."
        )

    def test_generic_exception(self):
        self.assertRaises(Exception, lambda: (self.genericCard.execute_action("player")))

    def test_looking_for_handmaid(self):
        self.assertIn(self.player_2, self.game.look_for_handmaid())

    def test_card_drawn_has_a_player(self):
        card_to_draw = Guard()
        self.player_1.draw_card(card_to_draw)
        self.assertEqual(card_to_draw.player, self.player_1)

    def test_end_of_round_sets_player_to_none(self):
        self.king.player.reset_round()
        self.assertEqual(self.king.player, None)


class TestPrincess(unittest.TestCase):

    def setUp(self):
        self.princess = Princess()
        self.game = LoveLetterGame("me")
        self.player = self.game.players[0]
        self.player.cards.pop()
        self.player.cards.append(self.princess)
        self.princess.player = self.player

    def test_execute_action_knocks_out_player(self):
        self.princess.player = self.player
        self.princess.execute_action()
        self.assertFalse(self.player.is_active)

    def test_princess_show_instructions(self):
        instructions = "Princess input instructions:\n" \
                       "'card number'\n" \
                       "Example: 1"
        self.assertEqual(Princess.input_instructions, instructions)


class TestCountess(unittest.TestCase):

    def setUp(self):
        self.countess = Countess()
        self.game = LoveLetterGame("me")
        self.player = self.game.players[0]
        self.countess.player = self.player
        self.player.cards = []
        self.player.cards.append(self.countess)
        self.countess.player = self.player

    def test_must_discard_card_with_king(self):
        self.player.cards.append(King())
        self.assertTrue(self.countess.must_discard())

    def test_must_discard_card_without_king(self):
        # print(self.player.cards)
        self.player.cards.append(Baron())
        self.assertFalse(self.countess.must_discard())

    def test_countess_show_instructions(self):
        instructions = "Countess input instructions:\n" \
                       "'card number'\n" \
                       "example: 2"
        self.assertEqual(Countess.input_instructions, instructions)


class TestKing(unittest.TestCase):

    def setUp(self):
        self.king = King()
        self.game = LoveLetterGame("me")
        self.player_1 = self.game.players[0]
        self.player_1.cards.pop()
        self.player_1.cards.append(Countess())
        self.player_1.cards.append(self.king)
        self.king.player = self.player_1
        self.player_2 = self.game.players[1]
        self.player_2.cards.append(Guard())

    def test_switch_cards(self):
        self.king.execute_action(self.player_2)
        self.assertEqual(len(self.player_1.cards), 2)
        self.assertTrue("Countess" in card.name for card in self.player_1.cards)
        self.assertEqual(len(self.player_2.cards), 2)
        self.assertTrue("Guard" in card.name for card in self.player_2.cards)

    def test_king_show_instructions(self):
        instructions = "King input instructions:\n" \
                       "'card number-opponent number'\n" \
                       "example: 2-1"
        self.assertEqual(King.input_instructions, instructions)


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

    def test_baron_show_instructions(self):
        instructions = "Baron input instructions:\n" \
                       "'card number-opponent number'\n" \
                       "example: 1-2"
        self.assertEqual(Baron.input_instructions, instructions)


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

    def test_priest_show_instructions(self):
        instructions = "Priest input instructions:\n" \
                       "'card number-opponent number'\n" \
                       "Example: 1-2"
        self.assertEqual(Priest.input_instructions, instructions)


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

    def test_prince_show_instructions(self):
        instructions = "Prince input instructions:\n" \
                       "'card number-opponent number' or 'card-number'\n" \
                       "Example: 1-2 for opponent and 1 for choosing self"
        self.assertEqual(Prince.input_instructions, instructions)


class TestGuard(unittest.TestCase):

    def setUp(self):
        self.guard = Guard()
        self.prince = Prince()
        self.king = King()
        self.player_1 = Player()
        self.guard_1 = Guard()
        self.player_1.cards.append(self.prince)
        self.player_1.cards.append(self.guard)

    def test_guard_action_on_enemy_true(self):
        result = self.guard.execute_action(self.player_1, self.prince.name)
        self.assertEqual(result, True)

    def test_guard_action_on_enemy_false(self):
        result = self.guard.execute_action(self.player_1, self.king.name)
        self.assertEqual(result, False)

    def test_guard_action_on_enemy_dead(self):
        self.guard.execute_action(self.player_1, self.king.name)
        is_no_dead = self.player_1.is_active
        self.assertEqual(is_no_dead, True)

    def test_guard_action_on_enemy_no_dead(self):
        self.guard.execute_action(self.player_1, self.prince.name)
        is_no_dead = self.player_1.is_active
        self.assertEqual(is_no_dead, False)

    def test_guard_action_card_guard_type(self):
        result = self.guard.execute_action(self.player_1, Guard())
        self.assertEqual(result, False)

    def test_guard_show_instructions(self):
        instructions = "Guard input instructions:\n" \
                       "'card number-opponent number-guess of the card'\n" \
                       "example: 1-2-king"
        self.assertEqual(Guard.input_instructions, instructions)


class TestLoveLetterGame(unittest.TestCase):

    def setUp(self):
        self.game = LoveLetterGame("Me")

    def test_player_exsistence_when_init(self):
        number_of_players = 2
        result = len(self.game.players)
        self.assertEquals(number_of_players, result)

    def test_board_with_initial_situation(self):
        # human player
        self.game.players[0].cards.pop()
        self.game.players[0].cards.append(Princess())
        # pc player
        self.game.players[1].cards.pop()
        self.game.players[1].cards.append(Baron())
        expected_text = "Deck : 10 remaining cards\n" \
                        "Player: Me, Hearts: 0, Cards: 0-Princess \n" \
                        "Player: PC Player, Hearts: 0, Cards: 0-Baron "
        result_text = self.game.board
        self.assertEquals(expected_text, result_text)

    def test_check_winner_false(self):
        self.assertFalse(self.game.check_winner())

    def test_check_winner_true(self):
        self.game.players[1].hearts = 7
        self.assertTrue(self.game.check_winner())

    def test_next_turn_winner(self):
        self.game.players[0].hearts = 7
        self.game.players[1].hearts = 0
        self.assertEqual(self.game.next_turn(), "Me wins")

    def test_next_turn_not_winner(self):
        self.game.players[0].hearts = 1
        self.game.players[1].hearts = 1
        self.assertNotEqual(self.game.next_turn(), "Me wins")

    def test_end_of_round(self):
        self.game.reset_round()
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
            self.game.select_target(self.game.players[0].name)

    def test_play_with_one_parameter(self):
        self.princess = Princess()
        self.game.players[0].cards.pop()
        self.game.players[0].cards.append(self.princess)
        self.princess.player = self.game.players[0]
        self.game.play("0")
        self.assertEqual(self.game.players[0].is_active, False)

    def test_play_with_two_parameteres(self):
        self.priest = Priest()
        self.game.players[0].cards.pop()
        self.game.players[0].cards.append(self.priest)
        self.priest.player = self.game.players[0]
        text = self.game.players[1].cards[0].__str__()
        result = self.game.play("0-1")
        self.assertEqual(text, result)

    def test_play_with_three_parameteres(self):
        self.guard = Guard()
        self.king = King()
        self.game.players[0].cards.pop()
        self.game.players[0].cards.append(self.guard)
        self.game.players[1].cards.pop()
        self.game.players[1].cards.append(self.king)
        self.guard.player = self.game.players[0]
        result = self.game.play("0-1-King")
        self.assertEqual(result, True)

    def test_validate_effect_active(self):
        self.game.players[1].is_active = False
        with self.assertRaises(TargetInvalidException):
            self.game.validate_effect(self.game.players[1])

    def test_validate_effect_handmaid(self):
        self.game.players[1].discarded.append(Handmaid())
        with self.assertRaises(TargetInvalidException):
            self.game.validate_effect(self.game.players[1])

    def test_give_heart_to_max_card(self):
        self.game.players[0].cards[0] = Princess()
        self.game.players[1].cards[0] = Guard()
        self.assertEqual(self.game.players[0].hearts, 0)
        self.assertEqual(self.game.players[1].hearts, 0)
        alive = {
            self.game.players[0].name: self.game.players[0].show_card().score,
            self.game.players[1].name: self.game.players[1].show_card().score,
        }
        self.assertTrue(self.game.give_heart_to_max_card(alive))

    def test_check_if_end_round_1_alive(self):
        self.game.players[1].is_active = False
        self.assertEqual(self.game.check_if_end_round(), True)
        self.assertEqual(self.game.players[0].hearts, 1)

    def test_check_if_end_round_many_alives(self):
        guard = Guard()
        king = King()
        self.game.deck.cards = []
        self.game.players[0].cards.pop()
        self.game.players[1].cards.pop()
        self.game.players[0].cards.append(king)
        self.game.players[1].cards.append(guard)
        self.assertEqual(self.game.check_if_end_round(), True)
        self.assertEqual(self.game.players[0].hearts, 1)
        self.assertEqual(self.game.players[1].hearts, 0)

    def test_give_heart_to_max_card_enters_tie(self):
        self.game.players[0].cards[0] = Handmaid()
        self.game.players[1].cards[0] = Handmaid()
        self.assertEqual(self.game.players[0].hearts, 0)
        self.assertEqual(self.game.players[1].hearts, 0)
        alive = {
            self.game.players[0].name: self.game.players[0].show_card().score,
            self.game.players[1].name: self.game.players[1].show_card().score,
        }
        self.assertTrue(self.game.give_heart_to_max_card(alive))
        self.assertEqual(self.game.players[0].hearts, 0)
        self.assertEqual(self.game.players[1].hearts, 0)

    def test_give_heart_to_max_card_fails(self):
        notalive = {
            "player1": 3,
            "player2": 4,
        }
        self.assertFalse(self.game.give_heart_to_max_card(notalive))

    def test_give_heart_to_winner(self):
        self.assertEqual(self.game.players[0].hearts, 0)
        self.assertTrue(self.game.give_heart_to_winner("Me"))
        self.assertEqual(self.game.players[0].hearts, 1)

    def test_give_heart_to_winner_fails(self):
        self.assertEqual(self.game.players[0].hearts, 0)
        self.assertEqual(self.game.players[1].hearts, 0)
        self.assertFalse(self.game.give_heart_to_winner("Nobody"))
        self.assertEqual(self.game.players[0].hearts, 0)
        self.assertEqual(self.game.players[1].hearts, 0)

    def test_check_if_end_round_false(self):
        guard = Guard()
        king = King()
        self.game.players[0].cards.pop()
        self.game.players[1].cards.pop()
        self.game.players[0].cards.append(king)
        self.game.players[1].cards.append(guard)
        self.assertFalse(self.game.check_if_end_round())

    def test_check_if_end_round_tie(self):
        guard = Guard()
        self.game.deck.cards = []
        self.game.players[0].cards.pop()
        self.game.players[1].cards.pop()
        self.game.players[0].cards.append(guard)
        self.game.players[1].cards.append(guard)
        self.game.players[0].score = 5
        self.game.players[1].score = 0
        self.assertTrue(self.game.check_if_end_round())
        self.assertEqual(self.game.players[0].hearts, 1)
        self.assertEqual(self.game.players[1].hearts, 0)

    def test_tie_breaker(self):
        guard = Guard()
        self.game.deck.cards = []
        self.game.players[0].cards.pop()
        self.game.players[1].cards.pop()
        self.game.players[0].cards.append(guard)
        self.game.players[1].cards.append(guard)
        self.game.players[0].score = 5
        self.game.players[1].score = 0
        self.game.tiebreaker(["Me", "PC Player"])
        self.assertEquals(self.game.players[0].hearts, 1)
