#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv

    db = MySQLdb.connect(user=user[1], passwd=user[2], db=user[3], port=3306)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id".format(user[4])
    cur.execute(query)

    states = cur.fetchall()
    for state in states:
        print(state)
