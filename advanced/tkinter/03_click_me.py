#!/usr/bin/python3

# This example shows how to handle a basic event in a button.
# This basic example uses the command parameter to handle the click event
# with a function that do not have any parameters.

# Example inspired from: https://www.youtube.com/watch?v=VMP1oQOxfM0&t=1176s


import tkinter

window = tkinter.Tk()
window.title("Handling the click event!")
window.geometry('500x500')


def say_hi():
    tkinter.Label(window, text="Hello! I am here!").pack()

tkinter.Button(window, text="Click Me!", command=say_hi).pack()



window.mainloop()


