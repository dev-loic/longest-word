# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string

class Game:

    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if len(word) == 0:
            return False
        for letter in word:
            if letter not in self.grid:
                return False
        return True

if __name__=="__main__":
    game = Game()
    print(game.grid)
