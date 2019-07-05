from tkinter import *

root = Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)
sub_menu = Menu(main_menu)
main_menu.add_cascade(label='File', menu=sub_menu)
sub_menu.add_command()

root.mainloop()
