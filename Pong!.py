import tkinter as tk
import random
import time


counter = 0
counter1 = 0


root = tk.Tk()
root.title('Pong!')
root.resizable(0, 0)
root.wm_attributes('-topmost', 1)
canvas = tk.Canvas(root, width=500, height=400, bd=0, highlightthickness=0)
canvas.config(bg='black')
canvas.pack()
root.update()

canvas.create_line(250, 0, 250, 400, fill='white')


class Ball:
    def __init__(self, canvas, color, paddle, paddle1):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 232, 210)
        starts = [-3, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 3
        if position[3] >= self.canvas_height:
            self.y = -3
        if position[0] <= 0:
            self.score(True)
            self.x = 3
        if position[2] >= self.canvas_width:
            self.score(False)
            self.x = -3
        if self.hit_paddle(position) == True:
            self.x = 3
        if self.hit_paddle1(position) == True:
            self.x = -3

    def hit_paddle(self, position):
        paddle_position = self.canvas.coords(self, paddle.id)
        if position[1] >= paddle_position[1] and position[1] <= paddle_position[3]:
            if position[0] >= paddle_position[0] and position[2] <= paddle_position[2]:
                return True
            return False

    def hit_paddle1(self, position):
        paddle_position = self.canvas.coords(self, paddle1.id)
        if position[1] >= paddle_position[1] and position[1] <= paddle_position[3]:
            if position[0] >= paddle_position[0] and position[2] <= paddle_position[2]:
                return True
            return False

    def score(self, value):
        global counter
        global counter1

        if value == True:
            a = self.canvas.create_text(125, 40, text=counter, font=('Arial', 60), fill='white')
            canvas.itemconfig(a, fill='black')
            counter += 1
            a = canvas.create_text(125, 40, text=counter, font=('Arial', 60), fill='white')

        if value == False:
            a = self.canvas.create_text(375, 40, text=counter1, font=('Arial', 60), fill='white')
            canvas.itemconfig(a, fill='black')
            counter += 1
            a = canvas.create_text(375, 40, text=counter1, font=('Arial', 60), fill='white')

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 150, 30, 250, fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('d', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 0
        if position[3] >= 400:
            self.y = 0

    def turn_left(self, event):
        self.y = -3

    def turn_right(self, event):
        self.y = 3


class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470, 150, 500, 250, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 0
        if position[3] >= 400:
            self.y = 0

    def turn_left(self, event):
        self.y = 3

    def turn_right(self, event):
        self.y = -3


paddle = Paddle(canvas, 'blue')
paddle1 = Paddle1(canvas, 'blue')
ball = Ball(canvas, 'orange')


while True:
    ball.draw()
    paddle.draw()
    paddle1.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
