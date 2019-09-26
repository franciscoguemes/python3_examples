#!/usr/bin/python3

# In this example I will show how you can use databases to improve the "MCM (MOVIE COLLECTION MANAGER) LTD." that
# I did in the last example of the serialization.

import sqlite3


class Movie:

    # In Python is not allowed the method overload so to have many constructors you use default argument values.
    def __init__(self, db_id, title, year):
        self.db_id = db_id
        self.title = title
        self.year = year

    def show_information(self):
        print('{:04} -- {:^45} -- {:04}'.format(self.db_id, self.title, self.year))
        # print(self.year, " -- ", self.title)


class MovieCollection:

    def __init__(self, file_name):
        self.connexion = sqlite3.connect(DB_FILE)

    def delete_movie(self, db_id):
        cursor = self.connexion.cursor()
        # delete_statement = (f"DELETE FROM Movie WHERE id = {db_id}")
        # print(delete_statement)
        # cursor.execute(delete_statement)
        delete_statement = ("DELETE FROM Movie WHERE id = ?")
        cursor.execute(delete_statement, (db_id))
        self.connexion.commit()
        cursor.close()

    def add_movie(self, new_movie):
        cursor = self.connexion.cursor()
        insert_statement = "INSERT INTO Movie VALUES(NULL,?,?)"
        cursor.execute(insert_statement, (new_movie.title, new_movie.year))
        self.connexion.commit()
        cursor.close()

    def get_movie(self, db_id):
        cursor = self.connexion.cursor()
        select_statement = ("SELECT * FROM Movie WHERE id = ?")
        cursor.execute(select_statement, (db_id,))
        m = cursor.fetchone()
        movie = Movie(m[0], m[1], m[2])
        cursor.close()
        return movie

    def update_movie(self, updated_movie):
        cursor = self.connexion.cursor()
        update_statement = "UPDATE Movie SET title = ?, year = ? WHERE id = ?"
        cursor.execute(update_statement, (updated_movie.title, updated_movie.year, updated_movie.db_id))

        self.connexion.commit()
        cursor.close()

    def show_movies(self):
        cursor = self.connexion.cursor()

        select_statement = ("SELECT * FROM Movie")
        cursor.execute(select_statement)
        movie_collection = cursor.fetchall()
        cursor.close()

        if len(movie_collection) == 0:
            print("*************************************************************************")
            print("Your collection is empty :-(")
            print("*************************************************************************")
        else:
            print("*************************************************************************")
            print('{:>4} -- {:^45} -- {:4}'.format("ID", "TITLE", "YEAR"))
            print("*************************************************************************")
            for m in movie_collection:
                movie = Movie(m[0], m[1], m[2])
                movie.show_information()
            print("*************************************************************************")

    def close(self):
        self.connexion.close()


def append_movie(collection):
    print("-------------------------------------------------------------------------")
    title = input("Please introduce the title:")
    year = int(input("Please introduce the year:"))
    movie = Movie(None, title, year)
    collection.add_movie(movie)
    # print("The movie has been added...")
    # movie.show_information()


def delete_movie(collection):
    print("-------------------------------------------------------------------------")
    db_id = input("Please introduce the id of the movie to delete:")
    # TODO: Verify this id...
    collection.delete_movie(db_id)


def update_movie(collection):
    print("-------------------------------------------------------------------------")
    db_id = int(input("Please introduce the id of the movie to update:"))
    # TODO: Verify this id...

    movie = collection.get_movie(db_id)
    title = input("Please introduce the new title of the movie (Empty string for non modifying this field): ")
    year = input("Please introduce the new year of the movie (Empty string for non modifying this field): ")

    if not title and not year:
        print("There are no values to update!")
        return

    if not title:
        title = movie.title

    if not year:
        year = movie.year
    else:
        year = int(year)

    updated_movie = Movie(db_id, title, year)
    collection.update_movie(updated_movie)


def print_menu():
    print("MCM (MOVIE COLLECTION MANAGER) LTD.")
    print("Menu")
    print("     l -> list your movies")
    print("     a -> add a new movie")
    print("     u -> update a movie")
    print("     d -> delete a movie")
    print("     e -> exit")
    option = input("Choose your option:")
    switcher = {
        "e" : "exit",
        "l" : "list",
        "a" : "append",
        "u" : "update",
        "d" : "delete"
    }
    return switcher.get(option.lower(),None)



# Name of the DB file. Since I assume you executed the previous example to create the DB, the file name is the same.
DB_FILE = "MoviesDB.sqlite3"

# The MCM starts here...
my_collection = MovieCollection(DB_FILE)

stay_in_application = True
while stay_in_application:
    opt = print_menu()
    if opt is None:
        print("The supplied option is invalid!!! Please try again...")
    elif opt == "exit":
        print("Thank you for using MCM!!!")
        stay_in_application = False
    elif opt == "list":
        my_collection.show_movies()
    elif opt == "append":
        append_movie(my_collection)
    elif opt == "delete":
        delete_movie(my_collection)
    elif opt == "update":
        update_movie(my_collection)
    else:  # close DB connection...
        my_collection.close()


