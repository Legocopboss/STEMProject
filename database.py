# SQL Connection and stuff
import datetime
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
    if not resP:
        return "Error"
    else:
        switch = {
            1: resP[0],  # all
            2: (resP[0])[1],  # name
            3: (resP[0])[2],  # balance
        }
        return switch.get(opt, None)


def findByName(name, opt):
    # opt: 1= if they exist return true
    #   opt: 2= show all that exist
    cursor.execute(f"""SELECT * FROM `accountsDB` WHERE Name = '{name}';""")
    resN = cursor.fetchall()
    if opt == 1:
        if not resN:
            return False
        else:
            return True
    elif opt == 2:
        return resN
    else:
        return None


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


def changeUserName(idnumber, newName):
    oldName = printInfo(idnumber, 2)
    cursor.execute(f"""UPDATE accountsDB SET Name = '{newName}' WHERE ID='{idnumber}';""")
    connection.commit()
    return f"Successfully changed {oldName} to {newName}"


#
#   PURCHASE THINGS
#

def allItems():  # THIS IS FOR THE PURCHASE BUTTONS
    cursor.execute(f"""SELECT * FROM itemsDB;""")
    listL = cursor.fetchall()
    return listL


def printItemInfo(idNumber, opt):
    cursor.execute(f"""SELECT * FROM itemsDB WHERE ID='{idNumber}';""")
    resP = cursor.fetchall()
    if not resP:
        return "Error"
    else:
        switch = {
            1: resP[0],  # all
            2: (resP[0])[1],  # name
            3: (resP[0])[2],  # price
        }
        return switch.get(opt, None)


def checkName(name, opt):
    # opt 1=return true if they exist
    # opt 2 = return all that have the name
    cursor.execute(f"""SELECT * FROM itemsDB WHERE Item = '{name}';""")
    resN = cursor.fetchall()
    if opt == 1:
        if not resN:
            return False
        else:
            return True
    elif opt == 2:
        return resN
    else:
        return None


def checkItemID(id):
    cursor.execute(f"""SELECT * FROM itemsDB WHERE ID='{id}';""")
    resn = cursor.fetchall()
    if not resn:
        return False
    else:
        return True


def changeItem(id, name, price, edit):  # leave the other as None for edit
    print(f"{id}\n{name}\n{price}\n{edit}")
    if id is None:  # add item
        cursor.execute(f"""INSERT INTO itemsDB(`Item`, `Price`) VALUES ('{name}','{price}');""")
        return f"Successfully added item: {name} for price of {price}"
    elif edit and (name is not None or price is not None):  # edit item
        if name is None:  # edit price
            cursor.execute(f"""UPDATE itemsDB SET `Price`= '{price}' WHERE ID = '{id}';""")
            return f"Successfully edited the price of {printItemInfo(id, 2)} to {price}"
        elif price is None:  # edit name
            cursor.execute(f"""UPDATE itemsDB SET `Item`= '{name}' WHERE ID = '{id}';""")
            return f"Successfully edited the name of {printItemInfo(id, 3)} to {name}"
    else:  # remove item
        ct = 0
        removeIds = id.split(",")
        for rr in removeIds:
            cursor.execute(f"""DELETE FROM itemsDB WHERE ID='{rr}';""")
            ct += 1
        connection.commit()
        return f"Successfully removed '{ct}' items from database"

    connection.commit()


def newTransaction(IDNumber, purchases, total):
    ct = datetime.datetime.now()
    print(ct)
    name = printInfo(IDNumber, 2)
    balance = printInfo(IDNumber, 3)

    cursor.execute(
        f"""INSERT INTO transactionsDB VALUES ('none', '{name}', '{IDNumber}', '{purchases}', '{total}', '{(balance - total)}', '{ct}');""")
    connection.commit()
    cursor.execute(f"""UPDATE accountsDB SET Balance = Balance+{total} WHERE ID='{IDNumber}';""")
    connection.commit()


def newTransaction_WithDepos(IDNumber, amount):
    ct = datetime.datetime.now()
    print(ct)
    name = printInfo(IDNumber, 2)
    balance = printInfo(IDNumber, 3)
    # print(balance)
    cursor.execute(
        f"""INSERT INTO transactionsDB VALUES ('none', '{name}', '{IDNumber}', 'WITHDRAWL/DEPOSIT', '{amount}', '{(balance + amount)}', '{ct}');""")
    connection.commit()
    cursor.execute(f"""UPDATE accountsDB SET Balance = Balance+{amount} WHERE ID='{IDNumber}';""")
    connection.commit()
    return f"Successfully updated the balance of {name} to {printInfo(IDNumber, 3)}"


def transactionLog():
    cursor.execute(f"""SELECT * FROM transactionsDB;""")
    transL = cursor.fetchall()
    return transL
