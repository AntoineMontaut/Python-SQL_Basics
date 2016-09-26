'''
Unit 1 lesson 3 challenge
'''

import sqlite3 as lite
import pandas as pd

#connect to database
con = lite.connect("db_unit1_lesson3.db")
cur = con.cursor()

#drop tables if they already exist
cur.execute("DROP TABLE IF EXISTS cities")
cur.execute("DROP TABLE IF EXISTS weather")

#create tables
cur.execute("CREATE TABLE cities (name text, state text)")
cur.execute("CREATE TABLE weather (city text, year integer, \
warm_month text, cold_month text, average_high integer)")

#add values in tables
cities = (("Washington", "DC"), ("Houston", "TX"), ("Las Vegas", "NV"), ("Atlanta", "GA"))
weather = (("Washington", 2013, "July", "January", 66), ("Houston", 2013, "August", "January", 78), \
("Las Vegas", 2013, "July", "December", 81), ("Atlanta", 2013, "July", "January", 75))

cur.executemany("INSERT INTO cities (name, state) VALUES (?,?)", cities)
cur.executemany("INSERT INTO weather (city, year, warm_month, cold_month, average_high) \
VALUES (?,?,?,?,?)", weather)

#print list of warm_months and prompt user to choose month to display
cur.execute("SELECT DISTINCT warm_month FROM cities INNER JOIN weather")
months = cur.fetchall()
month_list = []
prompt_str = "Please choose the warm_month in the following list: ("
for month in months:
    month_list.append(month[0])
    prompt_str = prompt_str + str(month[0]) + ", "
prompt_str = prompt_str[:-2] + "): "
month = raw_input(prompt_str)
if month not in month_list:
    raise ValueError("Please select a month from the list provided")


#join tables and load data in DataFrame
#select city and state that have a specific warm_month
'''uses SQL command to filter data'''
cur.execute("SELECT city, state, warm_month FROM\
(cities INNER JOIN weather ON name=city)\
WHERE warm_month='{0}'".format(month))

rows = cur.fetchall()
cols = [desc[0] for desc in cur.description]
ds = pd.DataFrame(rows, columns=cols)

sentence = "The cities that are warmest in {0} are: ".format(month)
if len(ds) > 1:
    for index in xrange(len(ds) - 1):
        sentence = sentence + str(ds.city[index]) + " ," + str(ds.state[index]) + ", "
    sentence = sentence + "and " + str(ds.city[len(ds)-1]) + ", " + str(ds.state[len(ds)-1]) + "."
else:
    sentence = "The only city that is warmest in {0} is: ".format(month) + str(ds.city[0]) + " ," + str(ds.state[0]) + "."

print sentence
 