from tkinter import *

class GameArea:
    def __init__(self, window):
        self.game_area = Canvas(window, width=432, height=243, bg="black")
        self.game_area.grid(column=0, row=0)


    def create_play_area(self):
        self.game_area.configure(bg="orange")
        return self.game_area

    def delete(self):
        self.game_area.delete("all")