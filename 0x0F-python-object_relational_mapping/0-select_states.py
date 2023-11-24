#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3300)
    curr = db.cursor()
    curr.execute("SELECT * FROM states")
    rows = curr.fetchall()
    for row in rows:
        print(row)
