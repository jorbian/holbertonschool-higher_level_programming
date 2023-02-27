
#!/usr/bin/python3
"""
LISTS CITIES OF DATABASE 'hbtn_0e_4_usa' ordered by city id.
"""
import sys
import MySQLdb

if __name__ == "__main__":

    database = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = database.cursor()
    cursor.execute(
            """SELECT C.id, C.name, S.name
            FROM cities C
            INNER JOIN states S
            ON C.state_id = S.id
            ORDER BY C.id"""
    )
    [print(city) for city in cursor.fetchall()]
