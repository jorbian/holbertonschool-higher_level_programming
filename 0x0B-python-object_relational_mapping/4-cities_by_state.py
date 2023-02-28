#!/usr/bin/python3
"""
LISTS CITIES OF DATABASE 'hbtn_0e_4_usa' ordered by city id.
"""
import sys
import MySQLdb

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = database.cursor()

    cursor.execute(
        'SELECT cities.id, cities.name, states.name \
        FROM cities LEFT JOIN states \
        ON cities.state_id = states.id'
    )
    [print(city) for city in cursor.fetchall()]