#!/usr/bin/python3

# In this first example I show how to create a DB with sqlite3 --> https://www.sqlite.org/index.html
# The steps are very easy
# 1- Open a connection to the DB
# 2- Create a cursor
# 3- Execute SQL statements
#   3.1- Create a table
#   3.2- Insert some rows in the table
# 4- Commit the changes
# 5- Close the connection to the DB

import sqlite3

# Name of the DB file. This may hold the relative or absolute path to the file. If it only contains the name
# of the file, then sqlite will create the file in the current working directory.
DB_FILE = "MoviesDB.sqlite3"

# It opens the connection to the DB, if the DB it does not exits it create the file called MyDatabase in the
# same directory.
my_connexion = sqlite3.connect(DB_FILE)

my_cursor = my_connexion.cursor()

try:
    # Create the table movies ...
    create_statement = """ CREATE TABLE Movie(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title VARCHAR(50) UNIQUE,
                            year INTEGER
                        )
                    """
    my_cursor.execute(create_statement)

    # Insert some movies with a parametrized sql statement. Note that the first value in the insert statement is
    # set to NULL. This is necessary since the field "id" is set to "AUTOINCREMENT" and therefore I must not
    # insert a value for it.
    insert_statement = "INSERT INTO Movie VALUES(NULL,?,?)"
    favourite_movies = [
        ("Master & Commander", 2003),
        ("Gladiator", 2000),
        ("Blade Runner", 1982),
        ("The Pursuit of Happyness", 2006)
    ]
    my_cursor.executemany(insert_statement, favourite_movies)

    # Commit the changes in the DB... This you could do it after every call to the method "execute" or "executemany"
    # but if you do not commit and close the connection all the changes will be gone.
    # See --> https://docs.python.org/3/library/sqlite3.html
    my_connexion.commit()

except sqlite3.OperationalError:
    print(F"The file {DB_FILE} already exists. Try to delete the file and execute again")

finally:
    # Finally I close the connection
    my_connexion.close()