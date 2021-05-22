from tkinter import *

class Paddle:
    def __init__(self, canvas):
        self.name = "paddle"
        self.img = PhotoImage(file="img/paddle1.png")
        self.dx = 2.5
        self.width = 74
        self.height = 16
        self.canvas = canvas

    def create_paddle(self, x, y):
        self.paddle = self.canvas.create_image(x -32, y, image=self.img, anchor=NW, tags="paddle")
        return self.paddle

    def move(self, key_presses):
        self.x, self.y = self.canvas.coords('paddle')

        self.canvas_width = self.canvas.cget('width')

        for key, val in key_presses.items():
            if val == 1:
                if key == 'Right':
                    self.canvas.coords('paddle', (min(368, self.x + 1 * self.dx), self.y))
                elif key == 'Left':
                    self.canvas.coords('paddle', (max(0, self.x - self.dx), self.y))

