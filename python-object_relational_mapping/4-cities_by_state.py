#!/usr/bin/python3
"""Module to list all cities"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Listing all cities in hbtn_0e_4_usa database"""

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities\
    LEFT JOIN states\
    ON cities.state_id = states.id\
    ORDER BY id ASC")
    cities_rows = cursor.fetchall()
    for row in cities_rows:
        print(row)
