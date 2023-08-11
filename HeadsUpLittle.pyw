import os
from tkinter import *
from PIL import ImageTk,Image  

global cwd
cwd = os.getcwd()

root = Tk()
root.iconbitmap("hud_icon_small.ico")
root.title('1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')

sb_open_2_5                 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\sb_open_2_5.png"))
bb_3bet_10                = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\bb_3bet_10.png"))
bb_call_2_5                    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\bb_call_2_5.png"))
sb_4bet                  = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\sb_4bet.png"))
sb_calls_3bet           = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\sb_calls_3bet.png"))
pushfold                = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\pushfold.png"))

# A Radiobutton to toggle between images
bigblinds = IntVar()

def call():
    canvas.delete(ALL)
    
    image = None
    if bigblinds.get() == 1:
        image = sb_open_2_5
    elif bigblinds.get() == 2:
        image = bb_3bet_10
    elif bigblinds.get() == 3:
        image = bb_call_2_5
    elif bigblinds.get() == 4:
        image = sb_4bet
    elif bigblinds.get() == 5:
        image = sb_calls_3bet
    elif bigblinds.get() == 6:
        image = pushfold
        
    if image:
        canvas.create_image(0, 0, anchor=NW, image=image)
        canvas.config(scrollregion=canvas.bbox(ALL))

  

R1=Radiobutton(root, text="1", variable=bigblinds, value=1, command=call)
R1.grid(row=1, column=0, sticky=N+E)
R2=Radiobutton(root, text="2", variable=bigblinds, value=2, command=call)
R2.grid(row=2, column=0, sticky=N+E)
R3=Radiobutton(root, text="3", variable=bigblinds, value=3, command=call)
R3.grid(row=3, column=0, sticky=N+E)
R4=Radiobutton(root, text="4", variable=bigblinds, value=4, command=call)
R4.grid(row=4, column=0, sticky=N+E)
R5=Radiobutton(root, text="5", variable=bigblinds, value=5, command=call)
R5.grid(row=5, column=0, sticky=N+E)
R6=Radiobutton(root, text="6", variable=bigblinds, value=6, command=call)
R6.grid(row=6, column=0, sticky=N+E)

canvas = Canvas(root, height=600, width=700,)
canvas.grid(column=5, row=0, rowspan=6, sticky=W)
canvas.create_image((2, 2), image=sb_calls_3bet, anchor=NW)

root.mainloop()