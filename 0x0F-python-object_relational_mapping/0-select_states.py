#!/usr/bin/python3
''' Lists all states from the database hbtn_0e_0_usa'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    query = cur.fetchall()
    for i in query:
        print(i)
    cur.close()
    db.close()
