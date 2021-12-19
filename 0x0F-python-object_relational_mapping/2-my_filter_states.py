#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    name = argv[4]
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""".format(name))

    query = cur.fetchall()

    for i in query:
        if i[1] == name:
            print(i)

    cur.close()
    db.close()
