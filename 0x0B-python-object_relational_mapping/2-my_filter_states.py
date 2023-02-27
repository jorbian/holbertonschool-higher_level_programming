#!/usr/bin/python3
"""
DISPLAY ALL VALUES IN 'states' TABLE OF DATABASE 'hbtn_0e_0_usa' WHOSE NAME
MATCHES VALUE SUPPLIED AS ARGUMENT:

USAGE: ./2-my_filter_states.py <username> <db_password> <db_name>
<state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) < 5:
        print("INSUFFICENT NUMBER OF ARGUMENTS")
    else:
        db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        c = db.cursor()
        c.execute(
            "SELECT * FROM `states` WHERE BINARY `name` = '{}'".format(
                sys.argv[4]
            )
        )
        [print(state) for state in c.fetchall()]
