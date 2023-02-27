#!/usr/bin/python3
"""
DISPLAY VALUES IN 'states' TABLE OF DATABASE 'hbtn_0e_0_usa' WHOSE
NAME MATCHES SUPPLIED ARGUMENT. SAFE FROM SQL INJECTIONS
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM states WHERE BINARY name = %(state)s ORDER BY id;',
        {'state': sys.argv[4]}
    )
    [print(state) for state in cursor.fetchall() if state[1] == sys.argv[4]]
