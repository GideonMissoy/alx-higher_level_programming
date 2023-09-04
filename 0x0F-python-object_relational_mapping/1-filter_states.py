#!/usr/bin/python3
"""
Script lists all states with a name starting with
N from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__name__':
    """
    Access the database and get the states.
    Lists all states with a name starting with `N`.
    """
    db = MySQLdb.connect(host='localhost', user=argv[1], port3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
