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
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        print(position)
        if position[1] <= 0:
            self.y = 3
        if position[3] >= self.canvas_height:
            self.y = -3
        if position[0] <= 0:
            self.x = 3
        if position[2] >= self.canvas_width:
            self.x = -3


ball = Ball(canvas, 'red')

while True:
    ball.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
