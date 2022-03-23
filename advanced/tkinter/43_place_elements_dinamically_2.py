#!/usr/bin/python3

# This is an example of place geometry where the elements are placed randomly
# No matter how many colors do you add to the array it will always display right

# Example inspired from: https://www.python-course.eu/tkinter_layout_management.php

import tkinter
import random



window = tkinter.Tk()
window.title("Placing elements dinamically")
window.resizable(False,False) # Prevent the window from being resized in the x or y axis


# You can add as many colors as you like from: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
colours = ['red','green','orange','white','yellow','blue','gold','salmon','dark turquoise','pale violet red']

r = 0
for c in colours:
   tkinter.Label(text=c, relief=tkinter.RIDGE, width=15).grid(row=r,column=0)
   tkinter.Entry(bg=c, relief=tkinter.SUNKEN, width=10).grid(row=r,column=1)
   r = r + 1



window.mainloop()