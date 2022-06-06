# SQL Connection and stuff

import random

import mysql.connector
from mysql.connector import Error


# customerLoginUI import run

def db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Database connect success")
    except Error as err:
        print(f"error: '{err}'")
    return connection


connection = db_connection("na02-db.cus.mc-panel.net", "db_441655", "edda40894a", "db_441655")
cursor = connection.cursor()


#
#   USER THINGS
#


def printInfo(idNumber, opt):
    cursor.execute(f"""SELECT * FROM accountsDB WHERE ID='{idNumber}';""")
    resP = cursor.fetchall()
    switch = {
        1: resP[0],
        2: (resP[0])[1],
        3: (resP[0])[2],
    }
    return switch.get(opt, None)


def checkLogin(idNumber):
    print("Id number is being checked in database")
    cursor.execute(f"""SELECT * FROM accountsDB WHERE ID='{idNumber}';""")
    return cursor.fetchall()


def newPerson(idNumber, name):
    print("adding new perosn to db")
    balance = random.randrange(25, 751)
    cursor.execute(f"""INSERT INTO accountsDB VALUES ('{idNumber}', '{name}', '{balance}');""")
    connection.commit()


#
#   ADMIN THINGS
#


def admFetchInfo(user, passw, opt):
    cursor.execute(f"""SELECT * FROM adminAccsDB WHERE Username='{user}' and Password='{passw}';""")
    res = cursor.fetchall()
    if not res:
        return None
    else:
        switch = {
            1: (res[0])[0],  # name
            2: ((res[0])[3], (res[0])[4]),  # adminTF & managerTF
        }
        return switch.get(opt, res[0])


def admCheckLogin(user, passw):
    res = admFetchInfo(user, passw, 5)
    if not res:
        return False, False
    else:
        if res[1]:
            return True, True
        if res[2]:
            return False, True


def viewTable(adm):  # adm is true then show admin table if false show accounts
    if adm:
        print("Admin list print")
        cursor.execute(f"""SELECT * FROM adminAccsDB;""")
    else:
        print("Accounts list print")
        cursor.execute(f"""SELECT * FROM accountsDB;""")
    viewT = cursor.fetchall()
    return viewT


def deleteUser(idNumbers):
    ct = 0
    removeIds = idNumbers.split(",")
    for rr in removeIds:
        cursor.execute(f"""DELETE FROM accountsDB WHERE ID='{rr}';""")
        ct += 1
    connection.commit()
    return f"Successfully removed '{ct}' users from database"


#
#   PURCHASE THINGS
#

def allItems():
    cursor.execute(f"""SELECT * FROM itemsDB;""")
    listL = cursor.fetchall()
    return listL
