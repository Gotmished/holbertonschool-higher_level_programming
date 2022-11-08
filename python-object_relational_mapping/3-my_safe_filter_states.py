#!/usr/bin/python3
"""
Module that accepts an argument and returns rows
from the states table that correspond. Protected
from MySQL injections
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    Returns rows from states table and is
    protected from SQL injection
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,user=username, \
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
    WHERE name =%(state_name)s \
    ORDER BY id ASC", {'state_name': state_name})
    state_rows = cursor.fetchall()
    for row in state_rows:
        print(row)
