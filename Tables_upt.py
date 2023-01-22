import pymysql
from datetime import datetime,timedelta
from tabulate import tabulate

conn=pymysql.connect(host='localhost',user='root',password='root',database='dbmsproject')
a=conn.cursor()

a.execute("insert into event values(1,'PesAThon',2022,'Season3');")
a.execute("insert into event values(2,'Swimming',2022,'Season3');")
a.execute("insert into event values(3,'Archery',2022,'Season3');");
a.execute("insert into event values(4,'Running100m',2020,'Season1');");
a.execute("insert into event values(5,'JavelinThrow',2021,'Season2');");

a.execute("insert into category values(1,'Under20',1);")
a.execute("insert into category values(1,'Under20',2);")
a.execute("insert into category values(1,'Under20',3);")
a.execute("insert into category values(2,'Under35',1);")
a.execute("insert into category values(2,'Under35',2);")
a.execute("insert into category values(2,'Under35',3);")
a.execute("insert into category values(2,'Under35',4);")
a.execute("insert into category values(3,'Under45',2);")
a.execute("insert into category values(3,'Under45',3);")
a.execute("insert into category values(3,'Under45',5);")

a.execute("insert into location values(1,'Bangalore','India',1);")
a.execute("insert into location values(2,'Tokyo','Japan',2);")
a.execute("insert into location values(3,'WashingtonDC','Usa',3);")
a.execute("insert into location values(4,'NewDelhi','India',4);")
a.execute("insert into location values(5,'LosAngeles','California',5);")
conn.commit()

