#!/usr/bin/python3
"""Connect to the hbtn_0e_0_usa database and print the states"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
         print(row)
