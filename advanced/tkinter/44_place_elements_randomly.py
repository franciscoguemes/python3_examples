#!/usr/bin/python3

# This is an example of place geometry where the elements are placed randomly


# Example inspired from: https://www.python-course.eu/tkinter_layout_management.php

import tkinter
import random

HEIGHT = 500
WIDTH = 600

LABEL_WIDTH=120
LABEL_HEIGHT=25

def get_random_color():
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    colour = '#' + "".join(ct_hex)
    return colour, brightness

def get_random_position():
    x=random.randint(0,WIDTH-LABEL_WIDTH)
    y=random.randint(0,HEIGHT-LABEL_HEIGHT)
    return x, y


window = tkinter.Tk()
window.title("Placing elements randomly")
window.resizable(False,False) # Prevent the window from being resized in the x or y axis

# By adding a canvas is a way to force the main window to have the defined size
canvas = tkinter.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

# You can add or delete as many languages as you want, the window will show them randomly. The more languages, the more chances of overlapping...
languages = ['Python','Perl','C++','Java','Tcl/Tk','C','Go','C++']
for i in range(len(languages)):
   bg_colour, brightness = get_random_color()
   x_position, y_position = get_random_position()
   l = tkinter.Label(window, 
                text=languages[i], 
                fg='White' if brightness < 120 else 'Black', 
                bg=bg_colour)
   l.place(x = x_position, y = y_position, width=LABEL_WIDTH, height=LABEL_HEIGHT)


window.mainloop()