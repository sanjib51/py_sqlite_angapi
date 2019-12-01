import os
import sqlite3

class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def db_connect():
    conn=sqlite3.connect('data/customer.db')
    #cursor=conn.cursor()
    conn.row_factory=dict_factory
    return conn

def close(conn):
    conn.commit()
    if(conn):
        conn.close()

def get_rows():
    conn=db_connect()
    cursor=conn.cursor()
    cursor.execute('select * from user;')

   # cursor.close()
   # close(conn)
   # jsondata={'user':[dict(zip(tuple(data.key()),i)) for i in data.fetchall()]}
    result=cursor.fetchall()
    print(result)
    return result
def add_user(u):
    conn=db_connect()
    cursor=conn.cursor()
    cursor.execute('insert into user(name, age, email) values(?,?,?);',u)
    lastrowid=cursor.lastrowid
    cursor.close()    
    conn.commit()
    return lastrowid

data = get_rows()



     
 