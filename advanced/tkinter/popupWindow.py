#!/usr/bin/python3

# This app shows how to show popup windows in Python.

import tkinter
from tkinter import Menu
from tkinter import messagebox


def additional_info():
    messagebox.showinfo("This is the title", "Version 2018")


def license_warning():
    messagebox.showwarning("License", "Product under GNU license")


def exit_app():
    answer = messagebox.askquestion("Exit", "Are you sure do you want to exit?")
    if answer == "yes":
        root.destroy()


def exit_app2():
    """
    This method works exactly the same as the method exit_app but in this case the method uses
    internally the askokcancel. The askokcancel returns a boolean value instead of "yes"/"no".
    :return:
    """
    answer = messagebox.askokcancel("Exit", "Are you sure do you want to exit?")
    if answer == True:
        root.destroy()


def close_document():
    answer = messagebox.askretrycancel("Try again", "Is not possible to close the document. It seems to be blocked")
    if answer == False:
        root.destroy()


root = tkinter.Tk()

menubar=Menu(root)
root.config(menu=menubar, width=500, height=300)

#The option tearoff removes the discontinuous line.
file_menu=Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as...")
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_document)
file_menu.add_command(label="Exit", command=exit_app)

edit_menu=Menu(menubar, tearoff=0)
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")

tools_menu=Menu(menubar, tearoff=0)
help_menu=Menu(menubar, tearoff=0)
help_menu.add_command(label="License", command=license_warning)
help_menu.add_command(label="About", command=additional_info)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="Tools", menu=tools_menu)
menubar.add_cascade(label="Help", menu=help_menu)

root.mainloop()


