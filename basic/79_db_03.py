#!/usr/bin/python3

# This example is a continuation of the previous one. Here I will show how to update information from the DB.
# The steps are very easy:
# 1- Open a connection to the DB
# 2- Create a cursor
# 3- Execute SQL statements: In this case an update statement
# 4- Commit the changes
# 5- Close the connection to the DB

import sqlite3

# Name of the DB file. Since I assume you executed the previous example to create the DB, the file name is the same.
DB_FILE = "MoviesDB.sqlite3"

# It opens the connection to the DB, if the DB it does not exits it create the file called MyDatabase in the
# same directory.
my_connexion = sqlite3.connect(DB_FILE)

my_cursor = my_connexion.cursor()

try:
    update_statement = ("UPDATE Movie SET year = 1983 WHERE title = 'Blade Runner'")
    my_cursor.execute(update_statement)

    # Commit the changes in the DB... This you could do it after every call to the method "execute" or "executemany"
    # but if you do not commit and close the connection all the changes will be gone.
    # See --> https://docs.python.org/3/library/sqlite3.html
    my_connexion.commit()

except sqlite3.OperationalError:
    print(F"The file {DB_FILE} does not exists. Please execute the previous examples.")

finally:
    # Finally I close the connection
    my_connexion.close()