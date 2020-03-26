import random as random


class Dice:
    def __init__(self):
        pass

    @staticmethod
    def shuffle():
        return random.randint(1, 6)
