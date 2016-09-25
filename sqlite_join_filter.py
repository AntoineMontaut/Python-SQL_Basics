'''
Join and filter data using sqlite
'''

import sqlite3 as lite
import pandas as pd

con = lite.connect("getting_started.db")
cur = con.cursor()

def to_pandas(cur):
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    return pd.DataFrame(rows, columns=cols)

def join_groupby():
    
    cur.execute("SELECT state, AVG(average_high) FROM\
    (cities INNER JOIN weather ON cities.name=weather.city) AS cit_wea\
    GROUP BY state")
    
    ds = to_pandas(cur)
    print ds
    
# join_groupby()

def order_by():

    cur.execute("SELECT state, AVG(average_high) FROM\
    cities INNER JOIN weather ON name=city\
    GROUP BY state ORDER BY AVG(average_high)")
    
    ds = to_pandas(cur)
    print ds
    
# order_by()

def filter_grouped():

    cur.execute("SELECT state, AVG(average_high) FROM\
    cities INNER JOIN weather ON name=city\
    GROUP BY state HAVING AVG(average_high)<65\
    ORDER BY AVG(average_high) DESC")
    
    ds = to_pandas(cur)
    print ds
    
filter_grouped()