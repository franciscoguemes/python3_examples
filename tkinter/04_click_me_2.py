#!/usr/bin/python3

# This example shows how to handle the left click mouse event to the button
# The mouse has 3 events:
#   <Button-1>  ---> left click
#   <Button-2>  ---> middle click
#   <Button-3>  ---> right click

# If you want to read further about events in tkinter:
#   https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

# Example inspired from: https://www.youtube.com/watch?v=VMP1oQOxfM0&t=1176s


import tkinter

window = tkinter.Tk()
window.title("Handling the left click event")
window.geometry('500x500')


def say_hi(event):
    tkinter.Label(window, text="Hello! I am here!").pack()


btn = tkinter.Button(window, text="Click Me!")
btn.bind("<Button-1>", say_hi) # 'bind' takes 2 parameters 1st is the event to handle and 2nd is the function
btn.pack()


window.mainloop()


