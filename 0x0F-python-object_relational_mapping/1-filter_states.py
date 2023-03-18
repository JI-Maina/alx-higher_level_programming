#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv

    db = MySQLdb.connect(user=user[1], passwd=user[2], db=user[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
