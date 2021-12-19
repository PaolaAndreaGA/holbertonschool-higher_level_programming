#!/usr/bin/python3
''' module 0'''


def getStates(userName, passWord, dbName):
    """lists all states from the database """

    import MySQLdb
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbName,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
        cur.close()
        db.close()


if __name__ == "__main__":
    """arguments and passes to get states from db"""
    from sys import argv

    getStates(argv[1], argv[2], argv[3])
