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


connection = db_connection("na02-db.cus.mc-panel.net", "db_603873", "8286175fe5", "db_603873")
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
    balance = random.randrange(3, 150)
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


def toggleAdminMan(AM, username):  # True for Admin False for Manager
    cursor.execute(f"""SELECT * FROM adminAccsDB WHERE Username='{username}';""")
    acc = cursor.fetchone()
    admin = bool(int(acc[3]))
    manager = bool(int(acc[4]))
    if AM:
        cursor.execute(f"""UPDATE adminAccsDB SET Admin = {not admin} WHERE Username='{username}';""")
        if not admin and not manager:
            connection.commit()
            cursor.execute(f"""UPDATE adminAccsDB SET Manager = {not manager} WHERE Username='{username}';""")
    else:
        cursor.execute(f"""UPDATE adminAccsDB SET Manager = {not manager} WHERE Username='{username}';""")
        if admin and manager:
            connection.commit()
            cursor.execute(f"""UPDATE adminAccsDB SET Admin = {not admin} WHERE Username='{username}';""")
    connection.commit()


def deleteAdminAccount(username):
    cursor.execute(f"""DELETE FROM adminAccsDB WHERE Username='{username}';""")
    connection.commit()


def addAdminAccount(name, admin, manager):
    splitName = str(name).split()
    firstN = splitName[0].lower()
    lastN = splitName[1].lower()
    username = firstN[0] + lastN
    password = firstN[0].upper() + "_@dminp@ssw0rd"

    cursor.execute(f"""INSERT INTO adminAccsDB VALUES ('{name}', '{username}', '{password}', {admin}, {manager});""")
    connection.commit()


def adminCheckName(name):
    cursor.execute(f"""SELECT * FROM adminAccsDB WHERE Name= '{name}'""")
    res = cursor.fetchall()
    if not res:
        return False
    else:
        return True


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


def newItem_VersionInventory(name, price, invenID):
    cursor.execute(f"""INSERT INTO `itemsDB_v2`(`Name`, `Price`, `InvenID`) VALUES ('{name}', '{price}', {invenID})""")
    connection.commit()
    return f"Successfully added {name} to POS with a price of {price}"


def removeItem_VersionInventory(id):
    cursor.execute(f"""SELECT * FROM itemsDB_v2 WHERE ID='{id}';""")
    item = cursor.fetchone()
    if not item:
        return
    else:
        cursor.execute(f"""DELETE FROM itemsDB_v2 WHERE ID='{id}';""")
        connection.commit()


def checkIfInvenIsInPOS(Invenid):  # if exists return true
    cursor.execute(f"""SELECT * FROM itemsDB_v2 WHERE InvenID='{Invenid}';""")
    idY = cursor.fetchall()
    if not idY:
        return False
    else:
        return True


def getItemFromInvenID(invenID):
    cursor.execute(f"""SELECT * FROM itemsDB_v2 WHERE InvenID='{invenID}';""")
    return cursor.fetchone()[0]


def allItems_VersionInventory():
    cursor.execute(f"""SELECT * FROM itemsDB_v2""")
    return cursor.fetchall()


def newTransaction(IDNumber, purchases, total):
    ct = datetime.datetime.now()
    print(ct)
    name = printInfo(IDNumber, 2)
    balance = printInfo(IDNumber, 3)

    cursor.execute(
        f"""INSERT INTO transactionsDB VALUES ('{name}', '{IDNumber}', '{purchases}', '{total}', '{(balance - total)}', '{ct}');""")
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
        f"""INSERT INTO transactionsDB VALUES ('{name}', '{IDNumber}', 'WITHDRAWL/DEPOSIT', '{amount}', '{(balance + amount)}', '{ct}');""")
    connection.commit()
    cursor.execute(f"""UPDATE accountsDB SET Balance = Balance+{amount} WHERE ID='{IDNumber}';""")
    connection.commit()
    return f"Successfully updated the balance of {name} to {printInfo(IDNumber, 3)}"


def transactionLog():
    cursor.execute(f"""SELECT * FROM transactionsDB;""")
    transL = cursor.fetchall()
    return transL


"""

INVENTORY THINGS

"""


def viewInventory():
    cursor.execute(f"""SELECT * FROM inventoryDB;""")
    invenV = cursor.fetchall()
    return invenV


def addInven(amt, id):
    cursor.execute(f"""UPDATE inventoryDB SET Stock = Stock+{amt} WHERE ID='{id}';""")
    connection.commit()


def getStock(id):
    cursor.execute(f"""SELECT * FROM inventoryDB WHERE ID='{id}';""")
    stock = cursor.fetchone()
    return stock[2]


def InventoryCHECK(id):
    cursor.execute(f"""SELECT * FROM inventoryDB WHERE ID='{id}';""")
    stock = cursor.fetchone()
    if stock[2] <= 5:
        removeItem_VersionInventory(id)


def checkInvenForID(id):
    cursor.execute(f"""SELECT * FROM inventoryDB WHERE ID = '{id}';""")
    resN = cursor.fetchall()
    if not resN:
        return False
    else:
        return True


def checkInvenForName(name, opt):
    # opt 1=return true if they exist
    # opt 2 = return all that have the name
    cursor.execute(f"""SELECT * FROM inventoryDB WHERE Merchandise = '{name}';""")
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


def addNewToInventory(name, amt):
    cursor.execute(f"""INSERT INTO inventoryDB(`Merchandise`, `Stock`) VALUES ('{name}',{amt});""")
    connection.commit()
    return f"Successfully added {name} into inventory with a starting value of {amt}"


def removeFromInventory(id):
    cursor.execute(f"""DELETE FROM inventoryDB WHERE ID='{id}';""")
    connection.commit()
    return f"Successfully removed item from inventory"


"""

SETTINGS THINGS

"""


def settings():
    cursor.execute(f"""SELECT * FROM settings;""")
    settR = cursor.fetchall()
    return settR


def getSetting(setID):
    cursor.execute(f"""SELECT * FROM settings WHERE ID = '{setID}';""")
    settR = cursor.fetchall()
    if not settR:
        return "ID Does not exist"
    else:
        return (settR[0])[1]


def toggleValue(id):
    cursor.execute(f"""SELECT * FROM settings WHERE ID = '{id}';""")
    setr = cursor.fetchall()
    if not setr:
        print("Error id doesnt exist")
    else:
        val = (setr[0])[1]
        newVal = 1 if val == 0 else 0
        cursor.execute(f"""UPDATE settings SET Value = {newVal} WHERE ID = '{id}';""")
        connection.commit()
        return f"Changed value of {(setr[0])[0]} to {(setr[0])[1]}"
