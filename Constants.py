class Constants(object):
    size = 3
    min_util = -1000
    max_util = +1000
    x_player = 'X'
    o_player = 'O'
    empty = ' '
    level = 2
    moves = 0

    cutOff_occurred = False
    max_depth_reached = 0
    total_nodes = 0
    pruning_max = 0
    pruning_min = 0

    infinity = 9999999999
    neg_infinity = -9999999999

    first = "h"

    def set_level(self, value):
        self.level = value

    def reset_state(self):
        self.cutOff_occurred = False
        self.max_depth_reached = 0
        self.total_nodes = 0
        self.pruning_max = 0
        self.pruning_min = 0

    def get_first(self):
        return self.first

    def set_first(self, value):
        self.first = value

    def get_size(self):
        return self.size

    def get_min_util(self):
        return self.min_util

    def get_max_util(self):
        return self.max_util

    def get_x_player(self):
        return self.x_player

    def get_o_player(self):
        return self.o_player

    def get_empty(self):
        return self.empty

    def get_level(self):
        return self.level

    def get_moves(self):
        return self.moves

    def get_cutOff_occurred(self):
        return self.cutOff_occurred

    def set_cutOff_occurred(self, value):
        self.cutOff_occurred = value

    def get_max_depth_reached(self):
        return self.max_depth_reached

    def get_total_nodes(self):
        return self.total_nodes

    def get_pruning_max(self):
        return self.pruning_max

    def increase_pruning_max(self):
        self.pruning_max += 1

    def get_pruning_min(self):
        return self.pruning_min

    def increase_pruning_min(self):
        self.pruning_min += 1

    def get_infinity(self):
        return self.infinity

    def get_neg_infinity(self):
        return self.neg_infinity

    def get_computer_player(self):
        return self.x_player

    def get_human_player(self):
        return self.o_player

    def increase_move(self):
        self.moves += 1

    def increase_total_nodes(self, value):
        self.total_nodes += value

    def set_max_depth_reached(self, value):
        self.max_depth_reached = value

    def change_player(self, player):
        if player == self.get_computer_player():
            return self.get_human_player()
        else:
            return self.get_computer_player()
