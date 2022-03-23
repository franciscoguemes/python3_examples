#!/usr/bin/python3

# Following the previous examples, in this example I am building a primitive software for managing your collection
# of movies. The software is able to read the movies from a file (deserialize) and to save the movies to a file
# (serialize)

import pickle


class Movie:

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def show_information(self):
        print(self.year, " -- ", self.title)


class MovieCollection:

    def __init__(self):
        self.movies = []

    def load_movies_from_file(self, file_name):
        binary_file = open(file_name, "ab+")
        binary_file.seek(0)
        try:
            self.movies = pickle.load(binary_file)
        except:
            print("The file is empty")
        finally:
            binary_file.close()
            del binary_file

    def save_movies_to_file(self, file_name):
        binary_file = open(file_name, "wb")
        pickle.dump(self.movies, binary_file)
        binary_file.close()
        del binary_file

    def length(self):
        return len(self.movies)

    def add_movie(self, new_movie):
        self.movies.append(new_movie)

    def show_movies(self):
        for m in self.movies:
            m.show_information()


def append_movie(collection):
    print("-------------------------------------------------------------------------")
    year = input("Please introduce the year:")
    title = input("Please introduce the title:")
    movie = Movie(title, year)
    collection.add_movie(movie)
    # print("The movie has been added...")
    # movie.show_information()


def print_collection(collection):
    if collection.length() == 0:
        print("*************************************************************************")
        print("Your collection is empty :-(")
        print("*************************************************************************")
    else:
        print("*************************************************************************")
        print("YEAR  --  TITLE")
        print("*************************************************************************")
        collection.show_movies()
        print("*************************************************************************")


def print_menu():
    print("MCM (MOVIE COLLECTION MANAGER) LTD.")
    print("Menu")
    print("     l -> list your movies")
    print("     a -> add a new movie")
    print("     s -> save to file")
    print("     e -> exit")
    option = input("Choose your option:")
    switcher = {
        "e" : "exit",
        "l" : "list",
        "s" : "save",
        "a" : "append",
    }
    return switcher.get(option.lower(),None)


# The MCM starts here...
MOVIES_FILE = "movies.data"
my_collection = MovieCollection()
my_collection.load_movies_from_file(MOVIES_FILE)

stay_in_application = True
while stay_in_application:
    opt = print_menu()
    if opt is None:
        print("The supplied option is invalid!!! Please try again...")
    elif opt == "exit":
        print("Thank you for using MCM!!!")
        stay_in_application = False
    elif opt == "list":
        print_collection(my_collection)
    elif opt == "append":
        append_movie(my_collection)
    else:  # save to file...
        my_collection.save_movies_to_file(MOVIES_FILE)




