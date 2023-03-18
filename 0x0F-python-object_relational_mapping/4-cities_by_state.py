#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa.
Results must be sorted in ascending order by cities.id
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities \
            LEFT JOIN states ON states.id=cities.state_id \
            ORDER BY cities.id")

    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()
