#!/usr/bin/python3
"""Module to list all states beginning with the letter N"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Prints rows in states table beginning with the letter N"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
    WHERE name LIKE 'N%' \
    ORDER BY id ASC")
    state_rows = cursor.fetchall()
    for row in state_rows:
        print(row)
