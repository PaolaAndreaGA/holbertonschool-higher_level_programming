#!/usr/bin/python3
'''
 script that takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 INNER JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s\
                 ORDER BY cities.id", (argv[4], ))
    query = cur.fetchall()
    first = 0
    for j in query:
        if first != 0:
            print(", ", end="")
            print("%s" % i, end="")
            first += 1
            print("")
    cur.close()
    db.close()
