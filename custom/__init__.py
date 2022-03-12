
import psycopg2

import variable

def createcon():
    conn = psycopg2.connect(database =variable.getdbname() , user =variable.getuname() , password = variable.getpass(), 
                                host = variable.getsource(), port = variable.getport())
    print("Opened database successfully")
    return conn,conn.cursor()
conn,cur=createcon()
def tcreate():
#create table
    cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY    NOT NULL,
      TODO           TEXT    NOT NULL,
      COMPLETED    BOOLEAN   NOT NULL)''')
    print("Table created successfully")
    conn.commit()

#insert into db
def insertd():
    cur.execute('''INSERT INTO COMPANY (ID,TODO,COMPLETED)
            VALUES (1,'Learn JS','y')''')

    cur.execute('''INSERT INTO COMPANY (ID,TODO,COMPLETED)
            VALUES (2,'Learn GIT','n')''')
    conn.commit()
    print("Records created successfully")

#retrive
def fetch():
    cur.execute("SELECT ID,TODO,COMPLETED  from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print ("TODO = ", row[1])
        print ("ADDRESS = ", row[2],"\n")
    print("Operation done successfully")


def deltable(tname):
    cur.execute("DELETE FROM "+tname)
    conn.commit()

#delete table
def tdel(tname):
    cur.execute("DROP TABLE "+tname)
    conn.commit()

conn.close()

