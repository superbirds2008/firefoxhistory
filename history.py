import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('places.sqlite')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT url, last_visit_date, title FROM moz_places')
    data = c.fetchall()
    for row in data:
        url=row[0]
        title=row[2]
        try:
            last_visit_date=datetime.datetime.fromtimestamp(row[1]/1000000)
        except:
            last_visit_date=time.ctime(row[1])
        print("|%-40s | %-60.60s | %-120.30s" %(last_visit_date, url, title))
        print('-'*170)
        

read_from_db()
