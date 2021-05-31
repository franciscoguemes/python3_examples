#!/usr/bin/python3

# This example shows how to serialize a collection of Strings into a binary file

import pickle

movies = ["Master & Commander", "Gladiator", "Blade Runner", "The Pursuit of Happyness"]

# I set the file extension to ".data" but could be any other extension or even not having any at all
binary_file = open("movies.data", "wb")

pickle.dump(movies, binary_file)

binary_file.close()

del binary_file
