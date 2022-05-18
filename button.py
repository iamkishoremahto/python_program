from tkinter import *

def printhello():
    print("Hello Button")

root= Tk()
root.geometry("750x530")
f1= Frame(root, borderwidth=3, relief= SUNKEN)
f1.pack(side= LEFT, anchor="nw")

b1= Button(f1, bg="yellow", command=printhello, fg="blue",  text= "Click me")
b1.pack(side= LEFT)
root.mainloop()
