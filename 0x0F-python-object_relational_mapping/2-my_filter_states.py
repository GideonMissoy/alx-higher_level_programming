#!/usr/bin/python3
"""
Script takes in an argument and displays all
values in the states where `name` matches the
argument from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    user, password, database, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=password, db=database)
    db = db.cursor()
    db.execute("""SELECT * FROM states
    WHERE name LIKE BINARY '{}' ORDER BY id"""
               .format(state))
    r = db.fetchall()
    for i in r:
        print(i)
