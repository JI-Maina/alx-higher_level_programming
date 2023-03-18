#!/usr/bin/python3
"""Safe script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (argv[4],))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
