from tkinter import *
def printval():
    with open("record.txt","a") as f:
        f.write(f"{name_var.get()} {phone_var.get()} {gender_var.get()} {paymentmode_var.get()} {checkboxval.get()}  \n")
    
root= Tk()
root.geometry("850x630")

Label(root,text= "Form", font="arial 13 bold").grid(row=0,column=3)
name = Label(root, text="Name")
phone = Label(root, text= "Phone")
gender = Label(root, text= "Gender")
paymentmode= Label(root, text= "Payment, Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column =2)
paymentmode.grid(row=4, column=2)

name_var= StringVar()
phone_var= StringVar()
gender_var= StringVar()
paymentmode_var= StringVar()
checkboxval= IntVar()


Entry(root,textvariable= name_var).grid(row=1, column=3)
Entry(root, textvariable= phone_var).grid(row=2, column=3)
Entry(root, textvariable= gender_var).grid(row=3, column=3)
Entry(root, textvariable=paymentmode_var).grid(row=4,column=3)
checkbox1= Checkbutton( text= "check", variable= "checkboxval")
checkbox1.grid(row=5,column=2)
Button(root, text= "Submit", command=printval).grid(row=6, column=3)



root.mainloop()