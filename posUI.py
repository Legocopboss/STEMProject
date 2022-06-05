from tkinter import *

root = Tk()
root.geometry("400x400")


# code in here
class button:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name


def run():
    return ""


bList = []
rTotal = 0


def newButton(bN, cA):
    bList.append(button(bN, cA))


def remButton(bN):
    bList.remove(button(bN))


def charge(cA):
    rTotal += cA


r = 0
c = 0
for b in range(len(bList)):
    bList[b] = Button(root, command=charge(b.getPrice), text=b.getName).grid(row=r, column=c).pack()
    if c == 5:
        c = 0
        r += 1
    else:
        c += 1

root.mainloop()
