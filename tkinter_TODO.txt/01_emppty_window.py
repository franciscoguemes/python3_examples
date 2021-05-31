#!/usr/bin/python3

# In case of not finding the packet Tkinter:
#	sudo apt-get install python3-tk
# See: https://stackoverflow.com/questions/25905540/importerror-no-module-named-tkinter
#
# How to move the window in the screen:
#   https://stackoverflow.com/questions/31797063/how-to-move-the-entire-window-to-a-place-on-the-screen-tkinter-python3
#

import tkinter


def main():
    root = tkinter.Tk()
    root.title(" My first Tkinter Window")
    root.geometry('500x200') # Set the size of the window to 500x100
    root.resizable(0, 0) # Don't allow resizing in the x or y direction
    # Place the window in the coordinates (100,100). Take into account that the origin of coordinates (0,0)
    # is the left upper corner of your screen.
    root.geometry('+100+100')

    # If you would like to add other widgets your code would go here...

    root.mainloop() # Keeps the dispatch events thread running


if __name__ == "__main__":
    main()