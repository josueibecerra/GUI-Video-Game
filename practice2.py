from tkinter import *

root = Tk()

label1 = Label(root, text='Name:')
label1.grid(row=0, column=0, sticky='E')

label2 = Label(root, text='password')
label2.grid(row=1, column=0, sticky='E')
entrySpace = Entry(root)
entrySpace.grid(row=0, column=1)
entrySpace2 = Entry(root)
entrySpace2.grid(row=1, column=1)

cbutton = Checkbutton(root, text='Remember password')
cbutton.grid(columnspan=2)

root.mainloop()
