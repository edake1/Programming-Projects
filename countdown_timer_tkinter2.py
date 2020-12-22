import sys
from tkinter import *
import time
import random

root = Tk()
root.title('2020 Countdown')
root.iconbitmap('C:\\Program Files\\Python39\\DLLs\\pyc.ico')
root.geometry('200x150')
root.config(background='orange')

l1 = Label(root, font='times 20', fg='blue')
l1.grid(row=1, column=2)

times = StringVar()
e1 = Entry(root, textvariable=times)
e1.grid(row=3, column=2)

t = 0


def set_timer():
    global t
    t += int(e1.get())
    return t


def countdown():
    global t
    if t > 0:
        # print(t)
        m, s = divmod(t, 60)
        h, m = divmod(m, 60)
        l1.config(text=str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2))
        t -= 1
        l1.after(1000, countdown)
    elif t == 0:
        print('end')
        l1.config(text='GO')


button1 = Button(root, text='SET', width=21, pady=5, bd=2, command=set_timer, fg='red')
button1.grid(row=4, column=2, padx=21)

button2 = Button(root, text='START', width=21, pady=5, bd=2, command=countdown, fg='red')
button2.grid(row=6, column=2, padx=21)

root.mainloop()
