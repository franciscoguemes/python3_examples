#!/usr/bin/python3

# This is an example of place geometry where the elements are placed dinamically regarding how many elments are in the array.

# Example inspired from: https://www.python-course.eu/tkinter_layout_management.php

import tkinter
import random


LABEL_WIDTH=120
LABEL_HEIGHT=25
Y_OFFSET = 5

def get_random_color():
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    colour = '#' + "".join(ct_hex)
    return colour, brightness


# You can add or delete as many languages as you want, the window will resize correctly according to the amount of languages
languages = ['Python','Perl','C++','Java','Tcl/Tk','C','Go','C++']

window = tkinter.Tk()
window.title("Placing elements dinamically")
window.resizable(False,False) # Prevent the window from being resized in the x or y axis


label_y= (LABEL_HEIGHT + Y_OFFSET)
total_height = len(languages) * label_y + Y_OFFSET
window.geometry("170x" + str(total_height) + "+" + str(Y_OFFSET) + "+" + str(Y_OFFSET)) 


for i in range(len(languages)):
   bg_colour, brightness = get_random_color()
   l = tkinter.Label(window, 
                text=languages[i], 
                fg='White' if brightness < 120 else 'Black', 
                bg=bg_colour)

   l.place(x = 20, y = Y_OFFSET + i*(LABEL_HEIGHT + Y_OFFSET), width=LABEL_WIDTH, height=LABEL_HEIGHT)



window.mainloop()