import imp
from tkinter import *
from turtle import left

root= Tk()
root.geometry("600x300")
root.minsize(300,150)
f1= Frame(root,bg="grey", borderwidth=3, relief= SUNKEN)
f1.pack(side=LEFT,fill = X)

l = Label(f1, text= " Label test", pady=15)
l.pack()

f2= Frame(root,bg="grey", borderwidth=3, relief=SUNKEN)
f2.pack(side=TOP, fill = Y)

l2 = Label(f2, text= " Label test", pady=115)
l2.pack(fill= X)



root.mainloop()