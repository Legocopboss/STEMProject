from tkinter import *

from database import *
from functionLibrary import *


def posUIDEF(idnum):
    root = Tk()
    root.geometry("400x400")

    first_frame = Frame(root)
    first_frame.pack(side=RIGHT, expand=1, fill=BOTH)
    trans_frame = Frame(root, width=100, height=400)
    trans_frame.pack(side=LEFT, expand=1, fill=BOTH)

    def removeFromTrans(item, price):
        currentTrans.remove([item, price])
        posUIDEF.currtotal = posUIDEF.currtotal - price
        updateTransaction()

    def updateTransaction():
        clear_frame(trans_frame)
        print(currentTrans)
        t = 1
        Label(trans_frame, text="Current\nTransaction", font='Helvetica 10 bold').grid(row=0, column=1)
        for aI in currentTrans:
            tempI = Button(trans_frame, text=aI, command=lambda it=aI[0], prc=aI[1]: removeFromTrans(it, prc)).grid(
                row=t, column=1)
            t = t + 1
        Label(trans_frame, text=f"Total: {posUIDEF.currtotal}", font='Helvetica 10 bold').grid(row=t + 1, column=1)
        if posUIDEF.currtotal > 0:
            Button(trans_frame, text="Confirm Purchase", font="Helvetica 8 bold", bg="lime",
                   command=confirmPurchase).grid(row=t + 2, column=1)

    def addPurchase(item, price):
        currentTrans.append([item, price])
        posUIDEF.currtotal = posUIDEF.currtotal + price
        print(posUIDEF.currtotal)
        updateTransaction()

    def confirmPurchase():
        purchasesT = sorted(currentTrans, key=lambda z: z[1], reverse=TRUE)
        purchases = str(purchasesT).replace('\'', '')
        print(purchases)
        newTransaction(idnum, purchases, -posUIDEF.currtotal)
        clear_frame(trans_frame)
        clear_frame(first_frame)
        exec(open("./customerLoginUI.py").read())

    posUIDEF.currtotal = 0.0
    currentTrans = []
    items = allItems()

    x = 0
    for li in items:
        print(li)
        templ = Button(first_frame, text=f"{li[0]}\n{li[1]}",
                       command=lambda it=li[0], prc=li[1]: addPurchase(it, prc)).grid(row=x, column=1)
        x = x + 1

    updateTransaction()

    root.mainloop()


if __name__ == "__customerLoginUI__":
    posUIDEF()
