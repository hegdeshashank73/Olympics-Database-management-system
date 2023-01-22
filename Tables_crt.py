import pymysql
from datetime import datetime,timedelta
from tabulate import tabulate

conn=pymysql.connect(host='localhost',user='root',password='root',database='dbmsproject')
a=conn.cursor()

a.execute("Create table Player(Pid int primary key, First_Name varchar(32), Last_Name varchar(32),Gender varchar(1),Weight float, Height float,Age int, Status varchar(10),Eid int);")
a.execute("Create table Event(Eid int primary key, Event_Name varchar(32),Year int, Season varchar(10));")
a.execute("Create table Location(Lid int, City varchar(32), Country varchar(32), Eid int not null);")
a.execute("Create table Category(Cid int, Category_Name varchar(32),Eid int not null);")
a.execute("Create table Medal(Pid int primary key, Medal_Won varchar(10), Cid int not null, Eid int not null);")
a.execute("Create table Approval(Pid int, TimeOfRegister datetime, Cid int, Eid int not null, Lid int);")
a.execute("Create table Suggestions(Name varchar(32), Suggestion varchar(200));")
conn.commit()

