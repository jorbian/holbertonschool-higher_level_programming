#!/usr/bin/python3
"""
DISPLAYS ALL CITIES OF GIVEN STATE FROM THE 'states' TABLE OF DATABASE
'hbtn_0e_4_usa.' -- SAFE FROM SQL INJECTIONS --
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
    cursor.execute("SELECT * FROM 'cities' as 'c' \
                   INNER JOIN 'states' as 's' \
                       ON 'c'.'state_id' = 's'.'id' \
                   ORDER BY 'c'.'id'")

    print(", ".join([ct[2] for ct in cursor.fetchall[4] == sys.argv[4]]))
