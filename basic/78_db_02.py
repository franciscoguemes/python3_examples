#!/usr/bin/python3

# This example is a continuation of the previous one. Here I will show how to retrieve information from the DB.
# The steps are very easy:
# 1- Open a connection to the DB
# 2- Create a cursor
# 3- Execute SQL statements: In this case a query
# 4- Handle the results of the query
# 5- Close the connection to the DB

import sqlite3

# Name of the DB file. Since I assume you executed the previous example to create the DB, the file name is the same.
DB_FILE = "MoviesDB.sqlite3"

# It opens the connection to the DB, if the DB it does not exits it create the file called MyDatabase in the
# same directory.
my_connexion = sqlite3.connect(DB_FILE)

my_cursor = my_connexion.cursor()

try:
    select_statement = ("SELECT * FROM Movie")
    my_cursor.execute(select_statement)
    my_movies = my_cursor.fetchall()

    print('{:>4} -- {:^45} -- {:4}'.format("ID", "TITLE", "YEAR"))
    for movie in my_movies:
        print('{:04} -- {:^45} -- {:04}'.format(movie[0], movie[1], movie[2]))

except sqlite3.OperationalError:
    print(F"The file {DB_FILE} does not exists. Please execute the previous example.")

finally:
    # Finally I close the connection
    my_connexion.close()