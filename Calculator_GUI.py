import tkinter as tk

root = tk.Tk()

blank = ''
equation = tk.StringVar()
calculation = tk.Label(root, textvariable=equation)

equation.set('Enter Your Equation')
calculation.grid(columnspan=4)


def button_press(num):
    global blank
    blank = blank + str(num)
    equation.set(blank)


def equal_press():
    try:
        global blank
        total = eval(blank)
        equation.set(total)
        blank = ''
    except SyntaxError:
        equation.set('Error')
    finally:
        pass


def clear_press():
    global blank
    equation.set('')
    blank = ''


Button0 = tk.Button(root, text='0', command=lambda: button_press(0))
Button1 = tk.Button(root, text='1', command=lambda: button_press(1))
Button2 = tk.Button(root, text='2', command=lambda: button_press(2))
Button3 = tk.Button(root, text='3', command=lambda: button_press(3))
Button4 = tk.Button(root, text='4', command=lambda: button_press(4))
Button5 = tk.Button(root, text='5', command=lambda: button_press(5))
Button6 = tk.Button(root, text='6', command=lambda: button_press(6))
Button7 = tk.Button(root, text='7', command=lambda: button_press(7))
Button8 = tk.Button(root, text='8', command=lambda: button_press(8))
Button9 = tk.Button(root, text='9', command=lambda: button_press(9))

Divide = tk.Button(root, text='/', command=lambda: button_press('/'))
Multiply = tk.Button(root, text='*', command=lambda: button_press('*'))
Subtract = tk.Button(root, text='-', command=lambda: button_press('-'))
Add = tk.Button(root, text='+', command=lambda: button_press('+'))
Decimal = tk.Button(root, text='.', command=lambda: button_press('.'))
Equal = tk.Button(root, text='=', command=equal_press)
Clear = tk.Button(root, text='C', command=clear_press)


Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)
Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)
Button0.grid(row=4, column=1)

Divide.grid(row=4, column=3)
Multiply.grid(row=3, column=3)
Subtract.grid(row=2, column=3)
Add.grid(row=1, column=3)
Decimal.grid(row=4, column=2)
Equal.grid(row=5, columnspan=4)
Clear.grid(row=4, column=0)

root.mainloop()
