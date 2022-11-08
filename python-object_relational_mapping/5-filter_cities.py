#!/usr/bin/python3
"""Module to list all cities in a particular state"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Listing all cities based upon state argument"""

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    state_name = argv[4]
    cursor.execute("SELECT cities.name\
    FROM cities\
    LEFT JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name =%(state_name)s \
    ORDER by cities.id ASC", {'state_name': state_name})
    cities_rows = cursor.fetchall()
    name_list = []
    for row in cities_rows:
        for city_name in row:
            name_list.append(city_name)
    print(', '.join(name_list))
