#!/usr/bin/python3
'''module 0 '''
import MySQLdb
from sys import argv


def Get_States(username, password, db_name):
    '''lists all states from the database hbtn_0e_0_usa'''

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states  ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()

    if __name__ == "__main__":
        """ take args and pass to states from db"""
        Get_States(argv[1], argv[2], argv[3])
