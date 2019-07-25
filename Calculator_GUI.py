import tkinter as tk

root = tk.Tk()

equation = tk.StringVar()
calculation = tk.Label(root, text=equation)

equation.set('23+54')
calculation.grid(columnspan=4)

root.mainloop()
