import time
from tkinter import Tk, Button
from tkinter.font import Font
from State import State
from SearchUtility import SearchUtility


class GUI:
    def __init__(self, input_constants):
        self.constants = input_constants
        self.searching = SearchUtility(input_constants)
        self.game = State(next_player=self.constants.get_human_player(), input_constant=self.constants)
        self.app = Tk()
        self.app.title('Tic Tac Toe')
        self.app.resizable(width=False, height=False)
        self.font = Font(family="Helvetica", size=32)
        self.buttons = {}

        for x, y in self.game.table:
            handler = lambda x_=x, y_=y: self.move(x_, y_)
            button = Button(self.app, command=handler, font=self.font, width=2, height=1)
            button.grid(row=x, column=y)
            self.buttons[x, y] = button
        self.update()

        if self.constants.get_first() == "c":
            self.game.nextPlayer = self.constants.get_computer_player()
            self.computer_move()

    def select_difficulty(self, value):
        self.constants.set_level(value)
        self.reset()

    def reset(self):
        self.resetStats()
        self.game = State(next_player=self.constants.get_human_player)
        self.update()
        self.app.destroy()

    def move(self, x, y):
        self.app.config(cursor="watch")
        self.app.update()
        self.game.table[x, y] = self.constants.get_human_player()
        self.game.nextPlayer = self.constants.get_computer_player()
        self.update()
        if self.searching.TERMINAL_TEST(self.game):
            return
        self.computer_move()

    def computer_move(self):
        if self.constants.get_level() == 3:
            self.game.depth = 0
            self.game = self.searching.ALPHA_BETA_SEARCH(self.game, time.time())
            self.printStats()
            self.resetStats()
        elif self.constants.get_level() == 2:
            if self.constants.get_moves() % 2 == 0:
                self.game = self.searching.RANDOM_PLAY(self.game)
            else:
                self.game = self.searching.ALPHA_BETA_SEARCH(self.game, time.time())
                self.printStats()
                self.resetStats()
            self.constants.increase_move()
        elif self.constants.get_level() == 1:
            self.game = self.searching.RANDOM_PLAY(self.game)
        self.update()
        self.app.config(cursor="")

    def update(self):
        for (x, y) in self.game.table:
            text = self.game.table[x, y]
            self.buttons[x, y]['text'] = text
            self.buttons[x, y]['disabledforeground'] = 'green'
            if text == self.constants.get_empty():
                self.buttons[x, y]['state'] = 'normal'
            else:
                self.buttons[x, y]['state'] = 'disabled'
        winning = self.searching.TERMINAL_TEST(self.game)
        if winning:
            winner = self.game.won(player=self.constants.change_player(self.game.nextPlayer))
            if winner:
                for x, y in winner:
                    self.buttons[x, y]['disabledforeground'] = 'red'
            for x, y in self.buttons:
                self.buttons[x, y]['state'] = 'disabled'
        for (x, y) in self.game.table:
            self.buttons[x, y].update()

    def mainloop(self):
        self.app.mainloop()

    def resetStats(self):
        self.constants.reset_state()

    def printStats(self):
        print("-----------------------")
        print("Statistics of the Move")
        print("Cutoff Occured:" + str(self.constants.get_cutOff_occurred()))
        print("Maximum Depth Reached:" + str(self.constants.get_max_depth_reached()))
        print("Total number of nodes generated:" + str(self.constants.get_total_nodes()))
        print("Number of times pruning occured within Max-Value:" + str(self.constants.get_pruning_max()))
        print("Number of times pruning occured within Min-Value:" + str(self.constants.get_pruning_min()))
