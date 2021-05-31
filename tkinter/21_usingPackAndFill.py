#!/usr/bin/python3

# In this example I am going to show how to use the option "fill" of the pack layout manager. The option fill is used to take all remaining space.
# The pack layout manager organizes the widgets in the block, which means that it occupies the entire available Width.

# Example inspired from: https://www.youtube.com/watch?v=VMP1oQOxfM0&t=985s

import tkinter

window = tkinter.Tk()
window.title("Using fill parameter with pack()")

# creating 3 simple Labels containing any text

# sufficient width
tkinter.Label(window, text="Suf. width", fg="white", bg="purple").pack()

# width of X
tkinter.Label(window, text="Taking all available X width", fg="white", bg="green").pack(fill = "x")

# height of Y
tkinter.Label(window, text="Taking all available Y height", fg="white", bg="black").pack(side="left", fill = "y")




window.mainloop()