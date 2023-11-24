#!/usr/bin/python3
"""
Script takes in args and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curr = db.cursor()
    match = argv[4]
    curr.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = curr.fetchall()
    for row in rows:
        print(row)
