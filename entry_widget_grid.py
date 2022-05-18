from tkinter import *
from tokenize import String

def getVal():
    print(f"{uservalue.get()}")
    print(f"{passvalue.get()}")
root= Tk()
root.geometry("750x560")

user=Label(root, text= "Username")
password= Label(root, text ="Password")
user.grid()
password.grid(row=1)

uservalue= StringVar()
passvalue= StringVar()

userentry = Entry(root, textvariable=  uservalue)
passentry = Entry(root, textvariable= passvalue)
userentry.grid(column=1, row=0)
passentry.grid(column=1, row=1)
submit= Button(root,text="Submit", command= getVal).grid()

root.mainloop()