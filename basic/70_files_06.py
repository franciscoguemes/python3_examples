#!/usr/bin/python3

# This example shows how to read and write from a file

from io import open

try:
    # The option "r+" is used for reading and writing from a file.
    text_file = open("myTextFile.txt", "r+")

    # Read all text from the file and store it in a variable
    text_before = text_file.read()

    # In the previous line we have read all the content in the file so we return the cursor to the beginning...
    text_file.seek(0)
    new_text = "This overrides the previous characters"
    # Now we override the first len(new_text) characters
    text_file.write(new_text)

    # Now we return the cursor to the beginning of the file in order to read the text again
    text_file.seek(0)
    text_after = text_file.read()

    # Do not forget to close the file when you are finished with it
    text_file.close()

    print("Text before...")
    print(text_before)
    print("Text after...")
    print(text_after)
except FileNotFoundError:
    print("The path you supplied does not exist")

