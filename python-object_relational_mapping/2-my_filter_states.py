#!/usr/bin/python3
"""
Module to display values in states table where
name corresponds to a partiular argument
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Returns values ordered by ID"""

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect("localhost", username, password, database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
    WHERE name LIKE BINARY '{}' \
    ORDER BY id ASC".format(state_name))
    state_rows = cursor.fetchall()
    for row in state_rows:
        print(row)
