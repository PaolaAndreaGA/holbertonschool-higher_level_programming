#!/usr/bin/python3
'''
lists all states with a name starting with N (upper N)
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states\
                 WHERE name LIKE 'N%'\
                 ORDER BY states.id")
    query = cur.fetchall()
    for i in query:
        if query[1][0] == 'N':
            print(i)
    cur.close()
    db.close()
