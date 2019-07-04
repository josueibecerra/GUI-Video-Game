from tkinter import *


def left_click(event):
    print('Left')


def right_click(event):
    print('Right')


def scroll(event):
    print('Scroll')


def left_key(event):
    print('Left Key Pressed')


def right_key(event):
    print('Right Key Pressed')


root = Tk()

root.geometry('500x500')
root.bind('<Button-1>', left_click)
root.bind('<Button-3>', right_click)
root.bind('<Button-2>', scroll)
root.bind('<Left>', left_key)
root.bind('<Right>', right_key)

root.mainloop()
