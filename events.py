from tkinter import *

def kishore(event):
    print(f"click button {event.x}  {event.y}")
root = Tk()
root.geometry("900x700")

widget= Button(root, text="Click Me")
widget.pack()
widget.bind('<Button-1>', kishore)
widget.bind('<Button-2>',quit)

root.mainloop()
