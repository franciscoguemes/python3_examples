#!/usr/bin/python3

# This example is the typical calculator application
# This is the calculator to build:
# #######
# 7 8 9 /
# 4 5 6 *
# 1 2 3 -
# 0 . + =

# Example inspired from: https://www.youtube.com/watch?v=VMP1oQOxfM0&t=1176s


import tkinter

window = tkinter.Tk()
#window.geometry("312x324")
window.resizable(0,0)
window.title("Calculator")

tkinter.Label(window, text="0", anchor="e", bg="orange").grid(row=0, columnspan=4, sticky="nswe") #The 'sticky' option forces the element to fill all extra space inside the grid

tkinter.Button(window, text="7").grid(row=1, column=0)
tkinter.Button(window, text="8").grid(row=1, column=1)
tkinter.Button(window, text="9").grid(row=1, column=2)
tkinter.Button(window, text="/").grid(row=1, column=3)

tkinter.Button(window, text="4").grid(row=2, column=0)
tkinter.Button(window, text="5").grid(row=2, column=1)
tkinter.Button(window, text="6").grid(row=2, column=2)
tkinter.Button(window, text="x").grid(row=2, column=3)

tkinter.Button(window, text="1").grid(row=3, column=0)
tkinter.Button(window, text="2").grid(row=3, column=1)
tkinter.Button(window, text="3").grid(row=3, column=2)
tkinter.Button(window, text="-").grid(row=3, column=3)

tkinter.Button(window, text="0").grid(row=4, column=0)
tkinter.Button(window, text=".").grid(row=4, column=1)
tkinter.Button(window, text="+").grid(row=4, column=2)
tkinter.Button(window, text="=").grid(row=4, column=3)

window.mainloop()