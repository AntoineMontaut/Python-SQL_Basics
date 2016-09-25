'''
Get version of sqlite3
'''

import sqlite3 as lite

con = lite.connect("getting_started.db")

with con:
    #assign cursor object to cur
    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    
    #fetch data from cursor using fetchone(); if more than one data, use fetchall()
    data = cur.fetchone()
    
    #print the result
    print("SQLite version: {0}".format(str(data)))