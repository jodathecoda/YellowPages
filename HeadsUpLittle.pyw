import os
from tkinter import *
from PIL import ImageTk,Image
import random

global cwd
cwd = os.getcwd()

selected_range = "sb_open_2_5"
separator = "   ...   odds:   "

root = Tk()
root.iconbitmap("hud_icon_small.ico")
root.title(selected_range + separator +'1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')

sb_open_2_5                 = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\sb_open_2_5.png"))
bb_3bet_10                = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\bb_3bet_10.png"))
bb_call_2_5                    = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\bb_call_2_5.png"))
sb_4bet                  = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\sb_4bet.png"))
sb_calls_3bet           = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\sb_calls_3bet.png"))
push10bb              = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\push10bb.png"))
call10bb              = ImageTk.PhotoImage(Image.open(cwd + "\\ranges\\call10bb.png"))

# A Radiobutton to toggle between images
bigblinds = IntVar()

def call():
    canvas.delete(ALL)
    
    image = None
    if bigblinds.get() == 1:
        image = sb_open_2_5
        selected_range = "sb_open_2_5"
        root.title(selected_range + separator +'1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')
    elif bigblinds.get() == 2:
        image = bb_3bet_10
        selected_range = "bb_3bet_10"
        root.title(selected_range + separator +'1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')
    elif bigblinds.get() == 3:
        image = bb_call_2_5
        selected_range = "bb_call_2_5"
        root.title(selected_range + separator +'1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')
    elif bigblinds.get() == 4:
        image = sb_4bet
        selected_range = "sb_4bet"
        root.title(selected_range + separator +'1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')
    elif bigblinds.get() == 5:
        image = sb_calls_3bet
        selected_range = "sb_calls_3bet"
        root.title(selected_range + separator +'1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')
    elif bigblinds.get() == 6:
        image = push10bb
        selected_range = "push10bb"
        root.title(selected_range + separator +'1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')
    elif bigblinds.get() == 7:
        image = call10bb
        selected_range = "call10bb"
        root.title(selected_range + separator +'1/4pot=17%  1/2pot=25%  1pot=33%  1.5pot=37.5%  2pot=40%')
        
        
    if image:
        canvas.create_image(0, 0, anchor=NW, image=image)
        canvas.config(scrollregion=canvas.bbox(ALL))

def randomizer():
   #rnd = random.uniform(1.0,99.9)
    rnd = random.randint(1,100)
    input_text.set(str(rnd)[0:5] + "%")

input_text = StringVar()

R1=Radiobutton(root, text="open", variable=bigblinds, value=1, command=call)
R1.grid(row=1, column=0, sticky=N+E)
R2=Radiobutton(root, text="raise", variable=bigblinds, value=2, command=call)
R2.grid(row=2, column=0, sticky=N+E)
R3=Radiobutton(root, text="call", variable=bigblinds, value=3, command=call)
R3.grid(row=3, column=0, sticky=N+E)
R4=Radiobutton(root, text="reraise", variable=bigblinds, value=4, command=call)
R4.grid(row=4, column=0, sticky=N+E)
R5=Radiobutton(root, text="call_3bet", variable=bigblinds, value=5, command=call)
R5.grid(row=5, column=0, sticky=N+E)
R6=Radiobutton(root, text="push<10bb", variable=bigblinds, value=6, command=call)
R6.grid(row=6, column=0, sticky=N+E)

R7=Radiobutton(root, text="call<10bb", variable=bigblinds, value=7, command=call)
R7.grid(row=7, column=0, sticky=N+E)

B7 = Button(root, text = "RAND", fg = "black", width = 15, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: randomizer()).grid(row = 7, column = 1, columnspan = 5, padx = 1, pady = 1)
I7 = Entry(root, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
I7.grid(row = 6, column = 2, columnspan = 5, padx = 1, pady = 1)

canvas = Canvas(root, height=600, width=700,)
canvas.grid(column=5, row=0, rowspan=6, sticky=W)
canvas.create_image((2, 2), image=sb_open_2_5, anchor=NW)

root.mainloop()