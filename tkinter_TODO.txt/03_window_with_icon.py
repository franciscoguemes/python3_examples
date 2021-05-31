#!/usr/bin/python3

# NOTE: If you want to see the icon in your system tray you need to execute this app from the terminal of your OS.
# If you execute this app from your IDE or the terminal inside your IDE then you will not see the icon.
#
#
# How to set an icon for your tkinter applicaiton
#   https://www.geeksforgeeks.org/iconphoto-method-in-tkinter-python/
#

import tkinter


def main():
    root = tkinter.Tk()

    # Get the icon. Only png, jpeg, jpg and ico files works.
    icon = tkinter.PhotoImage(file="resources/webserver.png")
    # Set the icon to the window
    root.iconphoto(True, icon)

    root.title(" A window with icon")
    root.geometry('500x200') # Set the size of the window to 500x100
    root.resizable(0, 0) # Don't allow resizing in the x or y direction

    # If you would like to add other widgets your code would go here...

    root.mainloop() # Keeps the dispatch events thread running


if __name__ == "__main__":
    main()