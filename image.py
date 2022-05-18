from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("550x450")
#photo =PhotoImage(file="pic.jpg")

image=Image.open("pic.jpg")
photo = ImageTk.PhotoImage(image)
img_lable= Label(image= photo)
img_lable.pack()
root.mainloop()