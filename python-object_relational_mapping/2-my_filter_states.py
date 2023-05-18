#!/usr/bin/python3
"""
DISPLAY ALL VALUES IN 'states' TABLE OF DATABASE 'hbtn_0e_0_usa' WHOSE NAME
MATCHES VALUE SUPPLIED AS ARGUMENT
"""
import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) < 5:
        sys.exit("INSUFFICENT NUMBER OF ARGUMENTS")

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM `states` WHERE BINARY `name` = '{}'".format(
                sys.argv[4]
                )
        )
    [print(state) for state in cursor.fetchall()]
