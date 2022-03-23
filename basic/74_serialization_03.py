#!/usr/bin/python3

# Following the previous examples, in this example I am going to show how to serialize objects.

import pickle


class Movie:

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def show_information(self):
        print(self.year, " -- ", self.title)


movie1 = Movie("Master & Commander", 2003)
movie2 = Movie("Gladiator", 2000)
movie3 = Movie("Blade Runner", 1982)
movie4 = Movie("The Pursuit of Happyness", 2006)
movies = [movie1, movie2, movie3, movie4]

# I set the file extension to ".data" but could be any other extension or even not having any at all
binary_file = open("movies.data", "wb")

pickle.dump(movies, binary_file)

binary_file.close()

del binary_file
