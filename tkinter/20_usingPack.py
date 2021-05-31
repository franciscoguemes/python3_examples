#!/usr/bin/python3

# This example is about showing how to use the pack layout manager.
# The pack layout manager organizes the widgets in the block, which means that it occupies the entire available Width.

# Example inspired from: https://www.youtube.com/watch?v=VMP1oQOxfM0&t=985s


import tkinter

window = tkinter.Tk()
window.title("Frames and pack() example")

# creating 2 frames TOP and BOTTOM

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")

# now, create some widgets in the top_frame and bottom_frame
btn1 = tkinter.Button(top_frame, text="Button1", fg="red").pack() # 'fg - foreground' is used to color the contents
btn2 = tkinter.Button(top_frame, text = "Button2", fg="green").pack() # 
btn2 = tkinter.Button(bottom_frame, text = "Button3", fg="purple").pack(side = "left") # 'side' is used to align the widgets
btn2 = tkinter.Button(bottom_frame, text = "Button4", fg="orange").pack(side = "left") #


window.mainloop()



