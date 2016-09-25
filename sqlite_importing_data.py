import sqlite3 as lite
import pandas as pd

cities = (("Washington", "DC"), ("Houston", "TX"), ("Las Vegas", "NV"), ("Atlanta", "GA"))
weather = (("Washington", 2013, "July", "January", 66), ("Houston", 2013, "July", "January", 78), \
("Las Vegas", 2013, "July", "December", 81), ("Atlanta", 2013, "July", "January", 75))

con = lite.connect("getting_started.db")
cur = con.cursor()

def insert_values():

    with con:
        cur.executemany("INSERT INTO cities VALUES (?,?)", cities)
        cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
        
# insert_values()

def retrieve_data():

    cur.execute("SELECT * FROM cities")
    
    #fetch data selected by cur
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
        
# retrieve_data()

def put_data_in_pandas():
    
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    
    ds = pd.DataFrame(rows, columns=cols)
    print(ds["name"][:3])
    
    
    
put_data_in_pandas()