from tkinter import *


root = Tk()


topFrame = Frame(root)
topFrame.pack()

botFrame = Frame(root)
botFrame.pack(side=BOTTOM)
botFrame.pack()

Button1 = Button(None, text='click me', bg='blue')
Button1.pack()

Button2 = Button(None, text='click me', bg='red')
Button2.pack(fill=X)

Button3 = Button(None, text='click me', bg='purple')
Button3.pack(side=RIGHT, fill=Y)

Button4 = Button(None, text='click me', bg='yellow')
Button4.pack()


root.mainloop()
