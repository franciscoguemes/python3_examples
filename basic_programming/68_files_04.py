#!/usr/bin/python3

# This example shows how to append text to an existing file

from io import open

try:
    # The option "a" is used for append text to an existing file, so the content will remain..
    text_file = open("myTextFile.txt", "a")

    line3 = "Extra line added to show the append method"
    new_line = "\n"

    text_file.write(new_line)
    text_file.write(line3)

    # Do not forget to close the file when you are finished with it
    text_file.close()

except FileNotFoundError:
    print("The path you supplied does not exist")

