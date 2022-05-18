from tkinter import *

root = Tk()
root.geometry("650x450")
root.title("Kishore")
root.minsize(230,150)


# lable opetion

# text - add the text
# bg- Background
# fg - foreground
# padx - x _Padding
# pady - y _Padding
# relief - border styling SUNKEN, RAISED, GROOVE, RIDGE

#Important pack option
#anchor="nw" "ne" "se" "sw"
# side = top, bottom, left, right
# fill = x 
lbl_text= Label(text='''Zuckerberg attended Harvard University, 
\n where he launched Facebook in February 2004 with his roommates Eduardo Saverin, 
\n Andrew McCollum, Dustin Moskovitz, and Chris Hughes. Originally launched to select college campuses,
\n the site expanded rapidly and eventually beyond colleges, reaching one billion users by 2012.
\n Zuckerberg took the company public in May 2012 with majority shares. In 2007, at age 23, 
\n he became the world's youngest self-made billionaire. As of March 2022, 
\n Zuckerberg's net worth was $74.5 billion according to the Forbes' Real Time Billionaires.''', bg="yellow", fg="blue", padx= 20, pady= 15, font="arial 8 bold", borderwidth=10, relief= SUNKEN)
lbl_text.pack(side="top", anchor="se", fill= X)

root.mainloop()