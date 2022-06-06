from tkinter import *

from database import *

root = Tk()
root.geometry("400x400")

first_frame = Frame(root)
first_frame.pack(expand=1, fill=BOTH)


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
    None


def remButton(bN):
    None


items = allItems()

x = 0
for li in items:
    Button(first_frame, text=f"{li[0]}\n{li[1]}", command=None).grid(row=2, column=x)

root.mainloop()
