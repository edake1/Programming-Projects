from tkinter import *

t = 0

root = Tk()
root.geometry('180x150')
label1 = Label(root, font='times 32')
label1.grid(row=1, column=2)


def set_timer():
    global t
    t += int(entry1.get())
    return t


def countdown():
    global t
    if t > 0:
        m, s = divmod(t, 60)
        h, m = divmod(m, 60)

        label1.config(text=str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2))
        t -= 1
        label1.after(1000, countdown)
    elif t == 0:
        print('End')
        label1.config(text='Goo')


times = StringVar()
entry1 = Entry(root, textvariable=times)
entry1.grid(row=3, column=2, columnspan=10)

button1 = Button(root, text='SET', width=40, command=set_timer)
button1.grid(row=4, column=2, padx=40)

button2 = Button(root, text='START', width=40, command=countdown)
button2.grid(row=6, column=2, padx=40)

root.mainloop()
