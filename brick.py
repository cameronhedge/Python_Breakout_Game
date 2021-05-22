from tkinter import *

class Brick:
    def __init__(self, canvas, color, num):
        self.name = f"brick{num}"
        self.canvas = canvas
        self.color = color
        self.img = PhotoImage(file = f"img/bricks/{color}.png")
        self.height = 16
        self.width = 32

    def create_brick(self, x, y):
        self.brick = self.canvas.create_image(x, y, image=self.img, anchor=NW, tags=self.name)
        return self.brick

    def destroy_brick(self):
        self.canvas.delete(self.name)