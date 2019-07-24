#!/usr/bin/python3


import tkinter
from tkinter import Label

top = tkinter.Tk()

top.title('Welcome to my examples')
top.geometry('500x100') #Set the size of the window to 500x500
top.resizable(0, 0) #Don't allow resizing in the x or y direction

# Add a label with the text...
label = Label(top, text="Hello World!")
label.grid(column=0, row=0)
label.pack()

top.mainloop()


