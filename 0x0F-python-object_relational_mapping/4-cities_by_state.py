#!/usr/bin/python3
"""
Script lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                        passwd=argv[2], db=argv[3], port=3306)
    curr = db.cursor()
    curr.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = curr.fetchall()
    for row in rows:
        print(row)
