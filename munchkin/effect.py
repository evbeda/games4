from board import Board


class Effect:

    def __init__(self):
        pass

    def apply_effect(self):
        raise NotImplementedError()


class DrawCardEffect(Effect):

    def apply_effect(self, deck=Board.treasure_deck, number_of_cards=1):

        cards = []
        for index in range(number_of_cards):
            cards.append(deck.pop())

        while Board.current_player.can_draw_cards() and cards:
            Board.current_player.draw_card(cards.pop())
        if len(cards) > 0:
            deck.cards.extend(cards)
