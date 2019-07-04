from tkinter import *




def print_name():
    print('Hello there Josue')

root = Tk()
button1 = Button(root, text='Click Me', command=print_name)
button1.pack()

root.mainloop()
