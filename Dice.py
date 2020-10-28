#Dice Bag
from tkinter import ttk
from tkinter import *

import random


#Defining each roll with their die
def roll20():
    val20 = str(random.randint(1,20))
    myLabel = Label(root, text= "D20: " + val20)
    myLabel.pack()
    rolls.append(myLabel)
def roll12():
    val12 = str(random.randint(1,12))
    myLabel = Label(root, text = "D12: " + val12)
    myLabel.pack()
    rolls.append(myLabel)
def roll10():
    val10 = str(random.randint(1,10))
    myLabel = Label(root, text = "D10: " + val10)
    myLabel.pack()
    rolls.append(myLabel)
def roll8():
    val10 = str(random.randint(1,8))
    myLabel = Label(root, text = "D8: " + val10)
    myLabel.pack()
    rolls.append(myLabel)
def roll6():
    val10 = str(random.randint(1,6))
    myLabel = Label(root, text = "D6: " + val10)
    myLabel.pack()
    rolls.append(myLabel)
def roll4():
    val10 = str(random.randint(1,4))
    myLabel = Label(root, text = "D4: " + val10)
    myLabel.pack()
    rolls.append(myLabel)
def clear():
    for x in range(len(rolls)-1, -1, -1):
        item = rolls[x]
        rolls.remove(item)
        item.destroy()

#list of labels
rolls = []

#GUI
root = Tk()
root.geometry("300x200")
root.title("Dice Bag")

#Creating buttons for our dice
bt1 = Button(root, text = "Roll D20", command = roll20)
bt2 = Button(root, text = "Roll D12", command = roll12)
bt3 = Button(root, text = "Roll D10", command = roll10)
bt4 = Button(root, text = "Roll D8", command = roll8)
bt5 = Button(root, text = "Roll D6", command = roll6)
bt6 = Button(root, text = "Roll D4", command = roll4)


#clear button
btclear = Button(root, text = "Clear Rolls", command = clear)
#modifier adding

#Formatting our dice.
bt1.grid(row = 1, column = 0)
bt2.grid(row = 2, column = 0)
bt3.grid(row = 3, column = 0)
bt4.grid(row = 4, column = 0)
bt5.grid(row = 5, column = 0)
bt6.grid(row = 6, column = 0)
btclear.grid(row = 7, column = 0)


root.mainloop()
