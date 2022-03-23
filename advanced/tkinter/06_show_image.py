#!/usr/bin/python3

# This example shows how to show a background image

# Example inspired from: https://www.youtube.com/watch?v=VMP1oQOxfM0&t=1176s


import tkinter

window = tkinter.Tk()
window.title("Binding the event to the button!")

# JPG image causes error
#icon = tkinter.PhotoImage(file='./resources/images/img_lights.jpg')

icon = tkinter.PhotoImage(file='./resources/images/road_PNG26.png')
label = tkinter.Label(window, image=icon)
label.pack()


window.mainloop()


