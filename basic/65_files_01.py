#!/usr/bin/python3

#   In this file I show how to create a file with a single line of text...

from io import open

try:
    # The option "w" creates the file if it does not exists, and if it exists overrides the content.
    text_file = open("myTextFile.txt", "w")
    line1 = "This is the text that will be written in the file"
    new_line = "\n"
    line2 = "This is the second line that will appear in the file"
    text_file.write(line1)
    text_file.write(new_line)
    text_file.write(line2)
    # Do not forget to close the file when you are finished with it
    text_file.close()
except FileNotFoundError:
    print("The path you supplied does not exist")

