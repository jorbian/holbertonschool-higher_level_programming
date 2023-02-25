#!/usr/bin/python3
""" LISTS STATES WITH NAME STARTING WITH 'N' FROM DATABASE 'hbtn_0e_0_usa.'
USAGE: ./1-filter_states.py $USERNAME $PASSWORD $DB_NAME
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
