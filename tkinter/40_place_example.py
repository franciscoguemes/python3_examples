#!/usr/bin/python3

# The place layout manager places the widgets at the specific position you want.

# Example inspired from: https://www.youtube.com/watch?v=D8-snVfekto&t=1479s
# For an in-detail explanation about place visit: https://effbot.org/tkinterbook/place.htm

import tkinter

HEIGHT = 700
WIDTH = 800

window = tkinter.Tk()
window.title("Using place()")

canvas = tkinter.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tkinter.Frame(window,bg="#80c1ff")
# On the X axis of the window, the frame will have:
#   10% margin on the left
#   it will take 80% of the width
#   10% margin on the right --> 100 - 10 -80 = 10
# On the Y axis of the window, the frame will have:
#   10% margin on top
#   It will take 50% of the height
#   40% margin on the bottom --> 100 - 10 - 50 = 40
frame.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.5) 


# The rest of the items in the application are positioned relatively to the frame

button = tkinter.Button(frame,text="Test button", bg="gray")
# On the X axis of the frame, the button will have:
#   0% margin on the left
#   it will take 25% of the frame's width
#   75% margin on the right --> 100 - 0 -25 = 75
# On the Y axis of the frame, the button will have:
#   0% margin on top
#   It will take 25% of the frame's height
#   75% margin on the bottom --> 100 - 0 -25 = 75
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)

label = tkinter.Label(frame, text="This is a label", bg="yellow")
label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)

entry = tkinter.Entry(frame, bg="green")
entry.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.2)

window.mainloop()