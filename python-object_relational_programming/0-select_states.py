#!/bin/python3
import MySQLdb as db
from sys import argv

'''
Simple module to make a connect to mysql server
with MySQLdb library
'''


conn = db.connect(host='localhost', port=3306, user=argv[1],
                  passwd=argv[2], db=argv[3])
cursor = conn.cursor()
cursor.execute('SELECT * FROM states ORDER BY states.id')
all_rows = cursor.fetchall()

for row in all_rows:
    print(row)
