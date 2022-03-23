#!/usr/bin/python3

# Following the previous examples, in this example I am going to show how to deserialize objects.
#   See the previous example to see how to serialize objects...

import pickle


class Movie:

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def show_information(self):
        print(self.year, " -- ", self.title)


# I set the file extension to ".data" but could be any other extension or even not having any at all
binary_file = open("movies.data", "rb")

movies = pickle.load(binary_file)

binary_file.close()

del binary_file

for movie in movies:
    movie.show_information()