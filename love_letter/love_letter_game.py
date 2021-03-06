from love_letter.deck import Deck
from love_letter.human_player import HumanPlayer
from love_letter.pc_player import PcPlayer
from love_letter.player import CountessNotDiscardedException


class TargetInvalidException(Exception):
    def __init__(self, message):
        self.message = message

hearts_to_win = {
    # number_of_players: hearts_to_win

    2: 7,
    3: 5,
    4: 4,
}


class LoveLetterGame:

    def __init__(self, name):
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.players = [HumanPlayer(name, self), PcPlayer(self)]
        # Logica de sacar cartas (regla del juego para 2 jugadores)
        if len(self.players) == 2:
            self.deck.remove_last()
            self.deck.show_three()

        for player in self.players:
            card = self.deck.draw_card()
            player.draw_card(card)

        self.current_player = self.players[0]

    def next_turn(self):
        text = ""
        if self.check_winner() and self.current_player.is_active:
            return "{} wins".format(self.current_player.name)
        if self.current_player.is_active:
            for index in range(len(self.current_player.cards)):
                text += str(index) + "-" + self.current_player.cards[index].__str__() + "\n"
            return "Its your turn\n" + text

    def play(self, command):
        try:
            commands = command.split("-")
            selected_card = self.current_player.select_card(commands[0])
            parameters = self.get_parameters(commands)
        except CountessNotDiscardedException:
            return "You must discard your Countess"
        except TargetInvalidException as e:
            return e.message
        result = selected_card.execute_action(*parameters)

        self.change_turn()        
        return result
        # lo que ingreso el usuario por input (puede ser mas de un valor)
        # return #-> el resultado de lo que ingreso el usuario: ejemplo: You Win

    def get_alive_players(self):
        return [player for player in self.players if player.is_active]

    def get_parameters(self, commands):
        parameters = []
        if len(commands) > 1:
            target = self.select_target(commands[1])
            self.validate_target(target)
            parameters.append(target)
        if len(commands) > 2:
            parameters.append(commands[2])
        return parameters

    def validate_target(self, player):
        if not player.is_active:
            raise TargetInvalidException(
                'Player {} is not active'.format(player.name)
            )

        if player in self.look_for_handmaid():
            raise TargetInvalidException(
                'Player {} has handmaid activated'.format(player.name)
            )
        return True

    def check_if_end_round(self):
        alive = {}
        for player in self.players:
            if player.is_active:
                alive[player.name] = player.show_card().score
        return len(alive) == 1 or len(self.deck.cards) == 0

    def give_heart_to_winner(self, winner):
        for player in self.players:
            if player.name == winner:
                player.hearts += 1
                return True
        return False

    def give_heart_to_max_card(self, alive):
        max_score = max(list(alive.values()))
        list_of_winners = []
        for player in self.players:
            if player.name in alive and player.show_card().score == max_score:
                list_of_winners.append(player.name)
        if len(list_of_winners) == 1:
            self.give_heart_to_winner(list_of_winners[0])
            return True
        elif len(list_of_winners) > 1:
            self.tiebreaker(list_of_winners)
            return True
        return False

    def tiebreaker(self, winners):
        max_score = 0
        winner = None
        for player in self.players:
            if player.name in winners and player.score > max_score:
                max_score = player.score
                winner = player.name
        self.give_heart_to_winner(winner)

    def look_for_handmaid(self):
        save_players = []
        for player in self.players:
            if (
                    len(player.discarded) > 0 and
                    player.discarded[0].name == "Handmaid"
            ):
                save_players.append(player)
        return save_players

    @property
    def board(self):
        text_to_show = "{}".format(self.deck.__str__())
        for player in self.players:
            text_to_show += "\n{}".format(player.__str__())
        # -> muestra al usuario el estado actual
        # del juego (no del feedback de lo que acaba de hacer)
        return text_to_show

    def reset_round(self):
        for player in self.players:
            player.reset_round()
        self.deck = Deck()
        self.deck.shuffle_cards()
        # Logica de sacar cartas (regla del juego para 2 jugadores)
        if len(self.players) == 2:
            self.deck.remove_last()
            self.deck.show_three()
        for player in self.players:
            card = self.deck.draw_card()
            player.draw_card(card)

    def check_winner(self):
        return len([player for player in self.players if player.hearts == hearts_to_win[len(self.players)]]) > 0

    def get_opponents(self):
        players_duplicate = self.players.copy()
        players_duplicate.remove(self.current_player)
        return players_duplicate

    def select_target(self, player_string_number):
        player_number = int(player_string_number)
        if player_number >= len(self.players) or player_number < 0:
            raise TargetInvalidException("The player selected doesn't exist")
        if self.players[player_number] is self.current_player:
            raise TargetInvalidException("You cannot be your own target")
        return self.players[player_number]

    def get_deck_card(self):
        return self.deck.draw_card()

    def change_turn(self):
        last_player_turn_index = self.players.index(self.current_player)
        if last_player_turn_index == len(self.players) - 1:
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[last_player_turn_index+1]
