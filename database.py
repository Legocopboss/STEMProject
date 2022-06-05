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


# run()


def printInfo(idNumber, opt):
    cursor.execute(f"""SELECT * FROM accountsDB WHERE ID='{idNumber}';""")
    resP = cursor.fetchall()
    all = resP[0]
    name = (resP[0])[1]
    balance = (resP[0])[2]
    switch = {
        1: all,
        2: name,
        3: balance,
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
