from tkinter import *
from tkinter import ttk, Label
from paddle import Paddle
from ball import Ball
from brick import Brick
from random import choice
import os

# --------------------- GAME VARIABLES --------------------- #
key_presses = {}
bricks = []
in_play = False
brick_colors = ['blue', 'green', 'grey', 'orange', 'purple', 'red']
patterns = [[4, 3, 2, 1], [8, 7], [5, 4, 3], [9]]
CANVAS_WIDTH, CANVAS_HEIGHT = 432, 243

# --------------------- INIT GAME WINDOW --------------------- #
root = Tk()
root.title("Breakout")

window = Frame(root)
window.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


game_area = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
game_area.grid(column=0, row=0)
game_area.configure(bg="orange")

def menu():
    game_area.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 - 12, text="Welcome to Breakout!", font=("Helvetica", 24, "bold"), tags="menu")
    game_area.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + 28, text="Press ENTER to start. Then SPACE to serve.", font=("Helvetica", 12, "italic"), tags="menu")

def start_game(e):
    global in_play, paddle, ball
    if not in_play:
        in_play = True
        # Create Paddle
        paddle = Paddle(game_area)
        paddle.create_paddle(432 / 2, 180)
        # Create Ball
        ball = Ball(game_area)
        ball.create_ball(220, 170)

        create_area()
        game_area.itemconfigure('end', text = "")
        game_area.itemconfigure('menu', text="")
        game_area.create_text(CANVAS_WIDTH - 30, CANVAS_HEIGHT - 20, text=" ".join(ball.lives), fill="blue",
                              font=("Helvetica", 10, "bold"), tags="lives")
        movement()


# --------------------- CREATE BRICK --------------------- #
def create_area():
    brick_count = 0
    pattern = choice(patterns)
    # Looks at the pattern array and creates a grid of bricks.
    for row, num in enumerate(pattern):
        color = choice(brick_colors)
        start_x = (432 - (num * 32) - ((num-1) * 16)) // 2
        start_y = 32
        for i in range(num):
            brick = Brick(game_area, color, brick_count)
            brick.create_brick(start_x + (i * 48), start_y + (row * 32))
            bricks.append(brick)
            brick_count += 1



def end_game():
    global in_play
    in_play = False

    if len(bricks) > 0:
        message = "Game Over"
    else:
        message = "You Win!"

    game_area.delete("all")
    game_area.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 - 12, text=message, font=("Helvetica", 24, "bold"), tags="end")
    game_area.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2 + 28, text="Press ENTER to restart", font=("Helvetica", 12, "italic"), tags="end")

# --------------------- MOVEMENT & COLLISIONS --------------------- #
def movement():
    if len(bricks) > 0:
        paddle.move(key_presses)
        ball.move(key_presses, paddle)
        # BALL x PADDLE COLLISIONS
        if ball.check_collision(paddle):
            ball.collision()
        # BALL x BRICKS COLLISIONS
        for brick in bricks:
            if ball.check_collision(brick):
                ball.collision()
                brick.destroy_brick()
                bricks.remove(brick)
    # If no more bricks - End Game
    if len(bricks) == 0 or len(ball.lives) == 0:
        return end_game()
    # Calls the function every 10ms
    window.after(10, movement)



# --------------------- KEYPRESS EVENTS --------------------- #
def key_event(e):
    key = e.keysym
    type = int(e.type)
    if type == 2:
        key_presses[key] = 1
    elif type == 3:
        key_presses[key] = 0

root.bind("<KeyPress>", key_event)
root.bind("<KeyRelease>", key_event)
root.bind("<Return>", start_game)

# --------------------- GAME --------------------- #
if __name__ == '__main__':
    menu()
    root.mainloop()
