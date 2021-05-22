from tkinter import *
import random

class Ball:
    def __init__(self, canvas):
        self.name = "ball"
        self.img = PhotoImage(file="img/ball.png")
        self.canvas = canvas
        self.dx = random.uniform(-1.75, 1.75)
        self.dy = -1.5
        self.height = 16
        self.width = 16
        self.started = False
        self.collisions = False
        self.lives = ["X", "X", "X"]

    def create_ball(self, x, y):
        self.ball = self.canvas.create_image(x, y, image=self.img, anchor=NW, tags="ball")
        return self.ball

    def reset(self):
        self.started = False
        self.collisions = False
        self.dy = -1.5
        paddle_x, paddle_y = self.canvas.coords('paddle')
        self.canvas.coords('ball', (paddle_x + 30, paddle_y - 10))

    def move(self, keypresses, paddle):
        self.x, self.y = self.canvas.coords('ball')

        # Sticks ball to paddle at start
        if not self.started:
            paddle_x, paddle_y = self.canvas.coords('paddle')
            self.canvas.coords('ball', (paddle_x + 30, paddle_y - 10))

        # Serves ball from paddle
        for key, val in keypresses.items():
            if key == 'space' and val == 1 and not self.started:
                self.started = True

        # Avoids paddle collision at serve.
        if self.started:
            if self.y < 150:
                self.collisions = True

            # Ball movement
            self.canvas.coords('ball', (self.x + self.dx, self.y + self.dy))

            # Top Collision
            if self.y <= 5:
                self.dy = 1.5
            # Paddle miss
            if self.y > 243:
                self.lives.pop()
                self.canvas.itemconfigure("lives", text = " ".join(self.lives))
                print(self.lives)
                self.reset()
            # Side Collisions
            # R/H
            if self.x > 426:
                self.canvas.coords('ball', (425, self.y))
                self.dx = -self.dx
            # L/H
            if self.x < 0:
                self.canvas.coords('ball', (5, self.y))
                self.dx = abs(self.dx)

    # Check if ball has collided with given target EG: Paddle or Brick
    def check_collision(self, target):
        self_x, self_y = self.canvas.coords('ball')
        target_x, target_y = self.canvas.coords(target.name)
        if self.collisions:
            if target_x > self_x + self.width or self_x > target_x + target.width:
                return False

            if target_y > self_y + self.height * 2/3 or self_y > target_y + self.height * 2/3:
                return False

            return True

    # Reaction to a collision
    def collision(self):
        if self.dy > 0:
            self.dy = -self.dy
        else:
            self.dy = 1.5



