#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb

db = MySQLdb.connect(host="root", passwd="root/root", db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(row)
