from tkinter import Tk, Button
from tkinter.font import Font
from GUI import GUI
from Constants import Constants


class Select:
    def __init__(self):
        self.constants = Constants()
        self.app = Tk()
        self.app.title('Select Who Goes First')
        self.app.geometry("70x70")
        self.app.eval('tk::PlaceWindow . center')
        self.font = Font(family="Helvetica", size=32)

        computer_handle = lambda: self.choose("c")
        human_handle = lambda: self.choose("h")
        b1 = Button(self.app, text='Computer', command=computer_handle)
        b1.grid(row=0, column=0, columnspan=20, sticky='WE')

        b2 = Button(self.app, text='Human', command=human_handle)
        b2.grid(row=1, column=0, columnspan=20, sticky='WE')

    def choose(self, option):
        self.constants.set_first(option)
        self.app.destroy()
        GUI(self.constants).mainloop()

    def mainloop(self):
        self.app.mainloop()
