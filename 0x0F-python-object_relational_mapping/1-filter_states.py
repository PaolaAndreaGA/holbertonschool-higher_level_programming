#!/usr/bin/python3
"""module 1"""

import MySQLdb


def Filter_States(username, password, db_name):
    """lists all states with a name starting with N from the database """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        chaset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    getStates(argv[1], argv[2], argv[3])
