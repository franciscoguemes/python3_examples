#!/usr/bin/python3

# This example shows how to read and process a text file line by line.

from io import open

try:
    # The option "r" is used for reading from the file, so no writing operations are allowed.
    text_file = open("myTextFile.txt", "r")
    # The read method reads all the text from the file and store each line in a list.
    lines = text_file.readlines()
    # Do not forget to close the file when you are finished with it
    text_file.close()
    for line in lines:
        # The argument end="" tells which character to print at the end of the line.
        print(line, end="")
    print("")
except FileNotFoundError:
    print("The path you supplied does not exist")

