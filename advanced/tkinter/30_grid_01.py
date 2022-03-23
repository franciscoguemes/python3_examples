#!/usr/bin/python3

# The grid layout manager organizes the widgets in a table-like structure.

# Example inspired from: https://www.youtube.com/watch?v=VMP1oQOxfM0&t=985s

import tkinter

window = tkinter.Tk()
window.title("Using grid()")

# creating 2 text labels and input labels

tkinter.Label(window, text="Username").grid(row=0) # this is placed in 0 0
# Entry to display the input-field
tkinter.Entry(window).grid(row=0, column=1) # this is placed in 0 1

tkinter.Label(window, text="Password").grid(row=1) # this is placed in 1 0
# Entry to display the password: https://stackoverflow.com/questions/2416486/how-to-create-a-password-entry-field-using-tkinter
tkinter.Entry(window, show="*").grid(row=1, column=1) # this is placed in 1 1

# 'Checkbutton' is used to create the check buttons
tkinter.Checkbutton(window, text="Keep Me Logged In").grid(columnspan=2) # 'columnspan' tells to take the width of 2 columns, you can also use 'rowspan'


window.mainloop()