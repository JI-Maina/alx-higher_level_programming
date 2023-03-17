#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

user = sys.argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=user[1], passwd=user[2], db=user[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()

    for row in rows:
        print(row)
