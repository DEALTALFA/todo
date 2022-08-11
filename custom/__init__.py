
import json
import psycopg2

from myvar import *

def createcon():
    conn = psycopg2.connect(database =getdbname() , user =getuname() , password =getpass(), 
                                host = getsource(), port = getport())
    print("Opened database successfully")
    return conn,conn.cursor()
conn,cur=createcon()


#create table

def tcreate():
    cur.execute('''CREATE TABLE COMPANY
      ( DETAIL json NOT NULL)''')
    print("Table created successfully")
    conn.commit()


#insert into db
# t={"name":"hello","course":"mca"}
def insertd(valuetoinsert):
    print(valuetoinsert)
    print("operation called")
    cur.execute('''INSERT INTO COMPANY (DETAIL)
            VALUES (%s)''',[json.dumps(valuetoinsert)])

    # cur.execute('''INSERT INTO COMPANY (ID,TODO,COMPLETED)
    #         VALUES (2,'Learn GIT','n')''')
    conn.commit()
    print("Records created successfully")


#retrive

def fetch():
    cur.execute("SELECT *  from COMPANY")
    # for data in cur.fetchall():
    #     print(data[0])
    return cur.fetchall()
    # rows = cur.fetchall()
    # for row in rows:
    #     print("ID = ", row[0])
    #     print ("TODO = ", row[1])
    #     print ("ADDRESS = ", row[2],"\n")
    print("Operation done successfully")


def deltable(tname):                #delete entry of table
    cur.execute("DELETE FROM "+tname)
    conn.commit()

#delete table
def tdel(tname):                    #delete table 
    cur.execute("DROP TABLE "+tname)
    conn.commit()
# tcreate()
# insertd(t)
#deltable("COMPANY")
#fetch()
#conn.close()

