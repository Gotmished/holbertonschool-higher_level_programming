#!/usr/bin/python3
"""
This module lists all states from
the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Returns rows from states table in order of ID"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    all_states = cursor.fetchall()
    for row in all_states:
        print(row)
