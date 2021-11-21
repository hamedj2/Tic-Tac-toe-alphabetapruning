import time
from random import randint
from copy import deepcopy
from State import State


class SearchUtility(object):

    def __init__(self, input_constant):
        self.constants = input_constant

    def ALPHA_BETA_SEARCH(self, state, start):
        v = self.MAX_VALUE(state=state, alpha=self.constants.get_min_util(), beta=self.constants.get_max_util(),
                           start=start)
        ret_val = list(filter(lambda x: x.value == v, state.children))[0]
        return ret_val

    def MAX_VALUE(self, state, alpha, beta, start):
        if self.TERMINAL_TEST(state=state):
            return self.UTILITY(state=state)

        duration = time.time() - start
        if duration >= 10:
            self.constants.set_cutOff_occurred(True)
            print(f"alpha:{alpha}, beta={beta}")
            return self.HEURISTIC(state)

        v = self.constants.get_neg_infinity()
        new_alpha = alpha
        state.children = self.ACTIONS(state)
        for a in state.children:
            v = max(v, self.MIN_VALUE(state=a, alpha=new_alpha, beta=beta, start=start))
            a.value = v
            if v >= beta:
                self.constants.increase_pruning_max()
                return v
            new_alpha = max(new_alpha, v)
        return v

    def MIN_VALUE(self, state, alpha, beta, start):
        if self.TERMINAL_TEST(state=state):
            return self.UTILITY(state=state)

        duration = time.time() - start
        if duration >= 10:
            self.constants.set_cutOff_occurred(True)
            print(f"alpha:{alpha}, beta={beta}")
            return self.HEURISTIC(state)

        v = self.constants.get_infinity()
        new_beta = beta
        state.children = self.ACTIONS(state)
        for a in state.children:
            v = min(v, self.MAX_VALUE(state=a, alpha=alpha, beta=new_beta, start=start))
            a.value = v
            if v <= alpha:
                self.constants.increase_pruning_min()
                return v
            new_beta = min(new_beta, v)
        return v

    def HEURISTIC(self, state):
        x3 = 0
        x2 = 0
        x1 = 0
        o3 = 0
        o2 = 0
        o1 = 0

        for r in range(0, self.constants.get_size()):
            os = 0
            xs = 0
            for c in range(0, self.constants.get_size()):
                if state.table[r, c] == self.constants.get_x_player():
                    xs += 1
                elif state.table[r, c] == self.constants.get_o_player():
                    os += 1

            if xs == 0:
                if os == 1:
                    o1 += 1
                elif os == 2:
                    o2 += 1
                elif os == 3:
                    o3 += 1

            if os == 0:
                if xs == 1:
                    x1 += 1
                elif xs == 2:
                    x2 += 1
                elif xs == 3:
                    x3 += 1

        for c in range(0, self.constants.get_size()):
            os = 0
            xs = 0
            for r in range(0, self.constants.get_size()):
                if state.table[r, c] == self.constants.get_x_player():
                    xs += 1
                elif state.table[r, c] == self.constants.get_o_player():
                    os += 1

            if xs == 0:
                if os == 1:
                    o1 += 1
                elif os == 2:
                    o2 += 1
                elif os == 3:
                    o3 += 1

            if os == 0:
                if xs == 1:
                    x1 += 1
                elif xs == 2:
                    x2 += 1
                elif xs == 3:
                    x3 += 1

        os = 0
        xs = 0
        for i in range(0, self.constants.get_size()):
            if state.table[i, i] == self.constants.get_x_player():
                xs += 1
            elif state.table[i, i] == self.constants.get_o_player():
                os += 1

        if xs == 0:
            if os == 1:
                o1 += 1
            elif os == 2:
                o2 += 1
            elif os == 3:
                o3 += 1

        if os == 0:
            if xs == 1:
                x1 += 1
            elif xs == 2:
                x2 += 1
            elif xs == 3:
                x3 += 1

        os = 0
        xs = 0
        for i in range(0, self.constants.get_size()):
            if state.table[self.constants.get_size() - i - 1, i] == self.constants.get_x_player():
                xs += 1
            elif state.table[self.constants.get_size() - i - 1, i] == self.constants.get_o_player():
                os += 1

        if xs == 0:
            if os == 1:
                o1 += 1
            elif os == 2:
                o2 += 1
            elif os == 3:
                o3 += 1

        if os == 0:
            if xs == 1:
                x1 += 1
            elif xs == 2:
                x2 += 1
            elif xs == 3:
                x3 += 1

        return (6 * x3 + 3 * x2 + x1) - (6 * o3 + 3 * o2 + o1)

    def TERMINAL_TEST(self, state):
        if state.is_full():
            return True

        if state.table[0, 0] == state.table[0, 1] \
                and state.table[0, 1] == state.table[0, 2] \
                and state.table[0, 0] != self.constants.get_empty():
            return True
        if state.table[1, 0] == state.table[1, 1] \
                and state.table[1, 1] == state.table[1, 2] \
                and state.table[1, 0] != self.constants.get_empty():
            return True
        if state.table[2, 0] == state.table[2, 1] \
                and state.table[2, 1] == state.table[2, 2] \
                and state.table[2, 0] != self.constants.get_empty():
            return True
        if state.table[0, 0] == state.table[1, 0] \
                and state.table[1, 0] == state.table[2, 0] \
                and state.table[0, 0] != self.constants.get_empty():
            return True
        if state.table[0, 1] == state.table[1, 1] \
                and state.table[1, 1] == state.table[2, 1] \
                and state.table[0, 1] != self.constants.get_empty():
            return True
        if state.table[0, 2] == state.table[1, 2] \
                and state.table[1, 2] == state.table[2, 2] \
                and state.table[0, 2] != self.constants.get_empty():
            return True
        if state.table[0, 0] == state.table[1, 1] \
                and state.table[1, 1] == state.table[2, 2] \
                and state.table[0, 0] != self.constants.get_empty():
            return True
        if state.table[0, 2] == state.table[1, 1] \
                and state.table[1, 1] == state.table[2, 0] \
                and state.table[0, 2] != self.constants.get_empty():
            return True
        return False

    def UTILITY(self, state):
        if state.table[0, 0] == state.table[0, 1] \
                and state.table[0, 1] == state.table[0, 2] \
                and state.table[0, 0] != self.constants.get_empty():
            return self.PLAYER_UTIL(state.table[0, 0])
        if state.table[1, 0] == state.table[1, 1] \
                and state.table[1, 1] == state.table[1, 2] \
                and state.table[1, 0] != self.constants.get_empty():
            return self.PLAYER_UTIL(state.table[1, 0])
        if state.table[2, 0] == state.table[2, 1] \
                and state.table[2, 1] == state.table[2, 2] \
                and state.table[2, 0] != self.constants.get_empty():
            return self.PLAYER_UTIL(state.table[2, 0])
        if state.table[0, 0] == state.table[1, 0] \
                and state.table[1, 0] == state.table[2, 0] \
                and state.table[0, 0] != self.constants.get_empty():
            return self.PLAYER_UTIL(state.table[0, 0])
        if state.table[0, 1] == state.table[1, 1] \
                and state.table[1, 1] == state.table[2, 1] \
                and state.table[0, 1] != self.constants.get_empty():
            return self.PLAYER_UTIL(state.table[0, 1])
        if state.table[0, 2] == state.table[1, 2] \
                and state.table[1, 2] == state.table[2, 2] \
                and state.table[0, 2] != self.constants.get_empty():
            return self.PLAYER_UTIL(state.table[0, 2])
        if state.table[0, 0] == state.table[1, 1] \
                and state.table[1, 1] == state.table[2, 2] \
                and state.table[0, 0] != self.constants.get_empty():
            return self.PLAYER_UTIL(state.table[0, 0])
        if state.table[0, 2] == state.table[1, 1] \
                and state.table[1, 1] == state.table[2, 0] \
                and state.table[0, 2] != self.constants.get_empty():
            return self.PLAYER_UTIL(state.table[0, 2])
        return 0

    def PLAYER_UTIL(self, player):
        if player == self.constants.get_computer_player():
            return self.constants.get_max_util()
        elif player == self.constants.get_human_player():
            return self.constants.get_min_util()
        return 0

    def RANDOM_PLAY(self, state):
        state.children = self.ACTIONS(state)
        ret_val = randint(0, len(state.children) - 1)
        return state.children[ret_val]

    def ACTIONS(self, state):
        children = []
        for i in range(0, self.constants.get_size()):
            for j in range(0, self.constants.get_size()):
                if state.table[i, j] == self.constants.get_empty():
                    child_table = deepcopy(state.table)
                    child_table[i, j] = state.nextPlayer
                    child_state = State(next_player=state.nextPlayer, input_constant=self.constants)
                    child_state.nextPlayer = self.constants.change_player(player=state.nextPlayer)
                    child_state.table = child_table
                    child_state.value = state.value
                    child_state.depth = state.depth + 1
                    self.constants.set_max_depth_reached(max(self.constants.get_max_depth_reached(), child_state.depth))
                    children.append(child_state)

        self.constants.increase_total_nodes(len(children))
        return children
