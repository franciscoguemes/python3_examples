#!/usr/bin/python3

# This example shows how to handle all the click events that a mouse can trigger on a button.
# The mouse has 3 events:
#   <Button-1>  ---> left click
#   <Button-2>  ---> middle click
#   <Button-3>  ---> right click

# If you want to read further about events in tkinter:
#   https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

# Example inspired from: https://www.youtube.com/watch?v=VMP1oQOxfM0&t=1176s


import tkinter

window = tkinter.Tk()
window.title("Handling all click events")
window.geometry('500x500')


def left_click(event):
    tkinter.Label(window, text="Left click!").pack()

def middle_click(event):
    tkinter.Label(window, text="Middle click!").pack()

def right_click(event):
    tkinter.Label(window, text="Right click!").pack()

btn = tkinter.Button(window, text="Click Me!")
btn.bind("<Button-1>", left_click)
btn.bind("<Button-2>", middle_click)
btn.bind("<Button-3>", right_click)
btn.pack()


window.mainloop()


