#!/usr/bin/python3

# This example shows how to read text from a file selecting the starting point in the file.

from io import open

try:
    # The option "r" is used for reading from the file, so no writing operations are allowed.
    text_file = open("myTextFile.txt", "r")

    # This set the cursor in the character that corresponds exactly with the half of the text in the file
    text_file.seek(len(text_file.read())/2)

    text = text_file.read()

    # Do not forget to close the file when you are finished with it
    text_file.close()

    print(text)
except FileNotFoundError:
    print("The path you supplied does not exist")

