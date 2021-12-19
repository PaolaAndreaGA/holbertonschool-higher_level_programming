#!/usr/bin/python3
"""module0"""

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

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    query = cursor.fetchall()

    for i in query:
        print(i)

    cursor.close()
    consult.close()
