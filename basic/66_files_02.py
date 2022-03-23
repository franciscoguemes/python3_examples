#!/usr/bin/python3

#   In this file I show how to read text from a text file

from io import open

try:
    # The option "r" is used for reading from the file, so no writing operations are allowed.
    text_file = open("myTextFile.txt", "r")
    # The read method reads all the text from the file at once.
    text = text_file.read()
    # Do not forget to close the file when you are finished with it
    text_file.close()
    print(text)
except FileNotFoundError:
    print("The path you supplied does not exist")

