from tkinter import *

def click(event):
    global scrvar
    text= event.widget.cget("text")
    print(text)
    if text == "=":
        pass
    elif text == "c":
        scrvar.set("")
        
    else:
        scrvar.set(scrvar.get() + text)
        screen.update()

root=Tk()
root.geometry("300x400")
root.minsize(300,400)
root.maxsize(300,400)
root.title("Calculator")
root.wm_iconbitmap("1.ico")

scrvar= StringVar()
scrvar.set("")
screen = Entry(root,textvar=scrvar, font="arial 25 bold" ).pack(padx=5, pady=10, fill= "both",)

btn_fr=Frame(root, bg ="grey")

b= Button(btn_fr, text="9", font= "arial 20 bold", padx= 10, pady=10)
b.pack(side= LEFT , padx=5, pady= 5)
b.bind('<Button-1>',click)
b= Button(btn_fr, text="8", font= "arial 20 bold", padx= 10, pady=10)
b.pack(side= LEFT , padx=5, pady= 5)
b.bind('<Button-1>',click)
b= Button(btn_fr, text="7", font= "arial 20 bold", padx= 10, pady=10)
b.pack(side= LEFT , padx=5, pady= 5)
b.bind('<Button-1>',click)

btn_fr.pack()

root.mainloop()