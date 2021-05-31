#!/usr/bin/python3

# This app simply generates a window with a menubar.
#   http://effbot.org/tkinterbook/menu.htm#Tkinter.Menu.add_command-method
#   http://effbot.org/tkinterbook/menu.htm#menu.Menu.add-method

import tkinter
from tkinter import Menu
from tkinter import Label


def handle_menu(menu):
    print(f"You clicked on \"{menu}\"")


root = tkinter.Tk()

menubar=Menu(root)
root.config(menu=menubar, width=500, height=300)

#The option tearoff removes the discontinuous line.
file_menu=Menu(menubar, tearoff=0)
#Note that in order to handle the event with a function that takes arguments it is necessary to use a lambda expression
file_menu.add_command(label="New", command=lambda:handle_menu("new"))
file_menu.add_command(label="Save", command=lambda:handle_menu("save"))
file_menu.add_command(label="Save as...")
file_menu.add_separator()
file_menu.add_command(label="Close")
file_menu.add_command(label="Exit", command=root.quit)

edit_menu=Menu(menubar, tearoff=0)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")

tools_menu=Menu(menubar, tearoff=0)
help_menu=Menu(menubar, tearoff=0)
help_menu.add_command(label="License")
help_menu.add_command(label="About")

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="Tools", menu=tools_menu)
menubar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
