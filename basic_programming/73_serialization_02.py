#!/usr/bin/python3

# This example shows how to read a collection of strings from a binary data. See the previous example to see
#   how to generate the binary file with a collection of strings.

import pickle

# Open the binary file in mode "rb" (read binary)
binary_file = open("movies.data", "rb")

movies = pickle.load(binary_file)

binary_file.close()

del binary_file

# Iterates over the collection of movies and print it...
for movie in movies:
    print(movie)


