#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s", (argv[4],))

    cities = cur.fetchall()

    # Retrieve all cities in a list
    # same as [city[0] for city in cities] in list comprehension
    foo = []
    for city in cities:
        foo += city

    # Then use join to separate with a comma
    foo = ", ".join(foo)
    print(foo)

    cur.close()
    db.close()
