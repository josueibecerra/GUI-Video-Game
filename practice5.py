from tkinter import *
root = Tk()


def evaluate():
    data = e.get()


e = Entry(root)

e.bind('<Return>')

ans = Label(root)
ans.pack()

root.mainloop()