import mysql.connector as sql
from datetime import datetime,timezone
print('\t\t\t\t\t\t\t\t\t\t\t\tEstablishing connection')
print()
try:
  conn=sql.connect(host='localhost',
                   user='root',
                   password='root',
                   database='Service_Station')
except:
  conn=sql.connect(host='localhost',
                   user='root',
                   password='root')
  c1=conn.cursor()
  c1.execute('create database Service_Station')

conn=sql.connect(host='localhost',
                 user='root',
                 password='root',
                 database='Service_Station')
if conn.is_connected():
  print("\t\t\t\t\t\t\t\t\t\t\t\tSuccessfully Connected")
c1=conn.cursor()
c1.execute('show tables;')
a=c1.fetchall()
if ('customer_details',) not in a:
  print('Customer details table seems to be missing')
  c1.execute('create table customer_details(sno varchar(30) primary key,\
name varchar(100),\
address varchar(1000),\
mobile varchar(25));') 
  print('table created')
elif ('vehicles',) not in a:
  print('Vehicles table seems to be missing')
  c1.execute("create table vehicles(sno varchar(200) ,model varchar(150) ,\
vehicle_number varchar(100),\
defect varchar(1000),\
total int,\
time_submitted char(19),\
vehicle_taken varchar(70));")
  print ('table created')

def add_customer(a,b,c,d):
    Insert = "insert into customer_details value('"+str(a)+"' , '"+str(b)+"' , '" +str(c)+"' , '"+ str(d)+"')"
    c1.execute(Insert)
    conn.commit()

def show_details(a):
  n=0
  select="select * from customer_details where sno='"+str(a)+"';"
  c1.execute(select)
  data=c1.fetchall()
  for row in data:
      for i in row:
        i=str(i)
        n=n+len(i)+1
        print(i,'  |  ' , end='')

def vehicle(a,b,c,d,e):
  utc_dt = datetime.now(timezone.utc)
  te= str(utc_dt.astimezone())
  x=''
  for i in range(0,16):
    x+=te[i]
  insert="insert into vehicles value('"+str(a)+"','"+str(b)+"','"+str(c)+"','"+str(d)+"','"+str(e)+"','"+str(x)+"','NOT TAKEN')"
  c1.execute(insert)
  conn.commit()

def search_vc(v):
  search="select sno from vehicles where vehicle_number='"+v+"';"
  c1.execute(search)
  a=c1.fetchall()
  for i in a :
    for j in i:
      j=int(j)
  show_details(j)

def update(v):
  utc_dt = datetime.now(timezone.utc)
  te= str(utc_dt.astimezone())
  x=''
  for i in range(0,16):
    x+=te[i]
  details = "select vehicle_taken from vehicles where vehicle_number = '"+str(v)+"';"
  c1.execute(details)
  data = c1.fetchall()
  if data[0][0] == "NOT TAKEN":
    update="update vehicles set vehicle_taken='Taken' where vehicle_number ='"+str(v)+"';"
    c1.execute(update)
    conn.commit()
    print(" Vehicle ",v," has been delivered now")
  else:
    print(" The vehicle ",v," was already given to the owner")
def check(a,x):
  if x==1:
    b="select * from customer_details where sno= '"+str(a)+"'"
    c1.execute(b)
    c=c1.fetchall()
    if len(c)==0:
      return False
    else:
      return True
  elif x==2:
    b="select * from vehicles where vehicle_number='"+str(a)+"'"
    c1.execute(b)
    c=c1.fetchall()
    if len(c)==0:
      return False
    else:
      return True   
  elif x==3:
    b="select * from customer_details where mobile='"+str(a)+"'"
    c1.execute(b)
    c=c1.fetchall()
    if len(c)==0:
      return False
    else:
      return True

def mobretrieve(a):
  b="select sno from customer_details where mobile="+str(a)+";"
  c1.execute(b)
  data=c1.fetchall()
  print("Customer Serial Number:",data[0][0])


def history(v):
  current="select defect from vehicles where vehicle_number='"+v+"';"
  c1.execute(current)
  data=c1.fetchall()
  n=0
  for row in data:
      for i in row:
        i=str(i)
        n=n+len(i)+1
        print(i,'  |  ' , end='')


def all_details():
  details="select * from customer_details Natural Join vehicles"
  c1.execute(details)
  data=c1.fetchall()
  for row in data:
      print(row)

def nottaken():
  details = "select * from customer_details Natural Join vehicles where vehicle_taken ='NOT TAKEN';"
  c1.execute(details)
  data=c1.fetchall()
  for row in data:
    print(row)








      




