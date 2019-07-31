import tkinter as tk
import random
import time

root = tk.Tk()
root.title('Bounce!')
root.resizable(0, 0)
root.wm_attributes('-topmost', 1)
canvas = tk.Canvas(root, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
root.update()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, position):
        paddle_position = self.canvas.coords(self.paddle.id)
        if position[2] >= paddle_position[0] and position[0] <= paddle_position[2]:
            if position[3] >= paddle_position[1] and paddle_position[3] <= paddle_position[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        print(position)
        if position[1] <= 0:
            self.y = 3
        if position[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(245, 100, text='Game Over')
        if position[0] <= 0:
            self.x = 3
        if position[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(position) == True:
            self.y = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        position = self.canvas.coords(self.id)
        if position[0] <= 0:
            self.x = 0
        if position[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2


paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.07)
