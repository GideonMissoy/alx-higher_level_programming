#!/usr/bin/python3
"""
Script that lists all states from the database hbtb_0e_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curr = db.cursor()
    curr.execute("""SELECT * FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY states.id""")
    rows = curr.fetchall()
    for row in rows:
        print(row)
