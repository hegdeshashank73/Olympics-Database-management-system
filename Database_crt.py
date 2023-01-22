import pymysql
from datetime import datetime,timedelta
from tabulate import tabulate

conn=pymysql.connect(host='localhost',user='root',password='root')
a=conn.cursor()
a.execute("create database dbmsproject;")
conn.commit()
