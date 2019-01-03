#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':

    """Connect to the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    """Create a cursor object"""
    cur = db.cursor()


    """Grab all cities in ascending order"""
    """"Results sorted in asc order by cities.id"""

    cur.execute("SELECT cities.name FROM cities LEFT OUTER JOIN states"+
    " ON cities.state_id=states.id WHERE states.name='{}'".format(sys.argv[4]))
    query_rows = cur.fetchall()
    list_a = []
    for row in query_rows:
        list_a.append(row[0])
    print (', '.join(list_a))
