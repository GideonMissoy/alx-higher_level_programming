#!/usr/bin/python3
"""
Script takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curr=db.cursor()
    curr.execute("""SELECT cities.name FROM
                 cities INNER JOIN states ON states.id=cities.states_id
                 WHERE states.name=%s""", (argv[4]))
    rows = curr.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
