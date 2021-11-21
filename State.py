import sys
from copy import deepcopy


class State:
    def __init__(self, next_player, input_constant, other=None):
        self.nextPlayer = next_player
        self.table = {}
        self.depth = 0
        self.utility = 0
        self.value = 0
        self.children = {}
        self.constants = input_constant

        for y in range(self.constants.get_size()):
            for x in range(self.constants.get_size()):
                self.table[x, y] = self.constants.empty

        if other:
            self.__dict__ = deepcopy(other.__dict__)

    def printBoard(self):
        for i in range(0, self.constants.get_size()):
            for j in range(0, self.constants.get_size()):
                if self.table[i, j] == self.constants.get_empty():
                    sys.stdout.write(' _ ')
                elif self.table[i, j] == self.constants.get_x_player():
                    sys.stdout.write(' X ')
                else:
                    sys.stdout.write(' O ')
            print("")

    def is_full(self):
        for i in range(0, self.constants.get_size()):
            for j in range(0, self.constants.get_size()):
                if self.table[i, j] == self.constants.get_empty():
                    return False

        return True

    def won(self, player):
        # horizontal
        for x in range(self.constants.get_size()):
            winning = []
            for y in range(self.constants.get_size()):
                if self.table[x, y] == player:
                    winning.append((x, y))
            if len(winning) == self.constants.get_size():
                return winning

        # vertical
        for y in range(self.constants.get_size()):
            winning = []
            for x in range(self.constants.get_size()):
                if self.table[x, y] == player:
                    winning.append((x, y))
            if len(winning) == self.constants.get_size():
                return winning

        # diagonal \
        winning = []
        for y in range(self.constants.get_size()):
            x = y
            if self.table[x, y] == player:
                winning.append((x, y))
        if len(winning) == self.constants.get_size():
            return winning

        # diagonal /
        winning = []
        for y in range(self.constants.get_size()):
            x = self.constants.get_size() - 1 - y
            if self.table[x, y] == player:
                winning.append((x, y))
        if len(winning) == self.constants.get_size():
            return winning

        # default
        return None
