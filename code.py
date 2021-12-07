import time
from tkinter import *
import tkinter as tk
from tkinter.ttk import *


window = Tk()
window.resizable(False, False)
window.title("River Crossing")
window.geometry('1000x1000')

lbl1 = Label(window, text=" ", font=("arail bold", 15))
lbl1.place(x=150, y=20)

lbl2 = Label(window, text=" ", font=("arail bold", 15))
lbl2.place(x=150, y=70)

lbl3 = Label(window, text=" ", font=("arail bold", 15))
lbl3.place(x=150, y=120)

lbl4 = Label(window, text=" ", font=("arail bold", 15))
lbl4.place(x=150, y=170)

lbl5= Label(window, text=" ", font=("arail bold", 15))
lbl5.place(x=150, y=220)

lbl6 = Label(window, text=" ", font=("arail bold", 15))
lbl6.place(x=150, y=270)

lbl7 = Label(window, text=" ", font=("arail bold", 15))
lbl7.place(x=150, y=320)

lbl8 = Label(window, text=" ", font=("arail bold", 15))
lbl8.place(x=150, y=370)

lbl9 = Label(window, text=" ", font=("arail bold", 15))
lbl9.place(x=150, y=420)

lbl10 = Label(window, text=" ", font=("arail bold", 15))
lbl10.place(x=150, y=470)

lbl11 = Label(window, text=" ", font=("arail bold", 15))
lbl11.place(x=600, y=20)

lbl12 = Label(window, text=" ", font=("arail bold", 15))
lbl12.place(x=600, y=70)

lbl13 = Label(window, text=" ", font=("arail bold", 15))
lbl13.place(x=600, y=120)

lbl14 = Label(window, text=" ", font=("arail bold", 15))
lbl14.place(x=600, y=170)

lbl15 = Label(window, text=" ", font=("arail bold", 15))
lbl15.place(x=600, y=220)

lbl16 = Label(window, text=" ", font=("arail bold", 15))
lbl16.place(x=600, y=270)

lbl17 = Label(window, text=" ", font=("arail bold", 15))
lbl17.place(x=600, y=320)

lbl18 = Label(window, text=" ", font=("arail bold", 15))
lbl18.place(x=600, y=370)

lbl19 = Label(window, text=" ", font=("arail bold", 15))
lbl19.place(x=600, y=420)

lbl20 = Label(window, text=" ", font=("arail bold", 15))
lbl20.place(x=600, y=470)

btn1 = tk.Button(window, text="manual show", bg="silver", fg='black', command=lambda: show(state_dict))
btn1.place(x=900, y=200)

btn2 = tk.Button(window, text="show path", bg="silver", fg='black', command=lambda: show_path(path1))
btn2.place(x=900, y=400)


state_array = [0, 1, 0, 0, 0, 0, 0, 0, 0]
state_dict = {
    "Boat": 0,
    "Father": 0,
    "Mother": 0,
    "FirstSon": 0,
    "SecondSon": 0,
    "FirstDaughter": 0,
    "SecondDaughter": 0,
    "Thief": 0,
    "Police": 0
}

path1 = [
    {
        "Boat": 0,
        "Father": 0,
        "Mother": 0,
        "FirstSon": 0,
        "SecondSon": 0,
        "FirstDaughter": 0,
        "SecondDaughter": 0,
        "Thief": 0,
        "Police": 0
    },
{
        "Boat": 1,
        "Father": 0,
        "Mother": 0,
        "FirstSon": 0,
        "SecondSon": 0,
        "FirstDaughter": 0,
        "SecondDaughter": 0,
        "Thief": 1,
        "Police": 1
    }

]


def waiting_time():
    time.sleep(3)


def show(state):
    if state['Boat'] == 0:
        lbl2.config(text='Boat')
    elif state['Boat'] == 1:
        lbl12.config(text='Boat')
    if state['Father'] == 0:
        lbl3.config(text='Father')
    elif state['Father'] == 1:
        lbl13.config(text='Father')
    if state['Mother'] == 0:
        lbl4.config(text='Mother')
    elif state['Mother'] == 1:
        lbl14.config(text='Mother')
    if state['Police'] == 0:
        lbl5.config(text='Police')
    elif state['Police'] == 1:
        lbl15.config(text='Police')
    if state['Thief'] == 0:
        lbl6.config(text='Thief')
    elif state['Thief'] == 1:
        lbl16.config(text='Thief')
    if state['FirstSon'] == 0:
        lbl7.config(text='First Son')
    elif state['FirstSon'] == 1:
        lbl17.config(text='First Son')
    if state['SecondSon'] == 0:
        lbl8.config(text='Second Son')
    elif state['SecondSon'] == 1:
        lbl18.config(text='Second Son')
    if state['FirstDaughter'] == 0:
        lbl9.config(text='First Daughter')
    elif state['FirstDaughter'] == 1:
        lbl19.config(text='First Daughter')
    if state['SecondDaughter'] == 0:
        lbl10.config(text='Second Daughter')
    elif state['SecondDaughter'] == 1:
        lbl20.config(text='Second Daughter')


def change(state, key, value):
    if state[key] != value:
        state[key] = value
    print(state)
    return state


def show_path(path):
    for state_in_path in path:
        show(state_in_path)
        waiting_time()


window.mainloop()

