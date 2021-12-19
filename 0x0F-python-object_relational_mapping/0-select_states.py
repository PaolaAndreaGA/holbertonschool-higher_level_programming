#!/usr/bin/python3
"""module0"""

import Py
import MySQLdb
from sys import argv

if __name__ == "__main__":

    consult = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    query = cur.fetchall()

    for i in query:
        print(i)

    cur.close()
    consult.close()
