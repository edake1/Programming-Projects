from tkinter import *

root = Tk()
root.title('SIMPLE CALCULATOR')
frame = LabelFrame(root, text="CALCULATOR", padx=20, pady=10)
frame.pack(padx=100, pady=50)


def my_Click():
    button0.configure(text = name.get())
    button1.configure(text = name.get())
    button2.configure(text=name.get())
    button3.configure(text=name.get())
    button4.configure(text = name.get())
    button5.configure(text = name.get())
    button6.configure(text = name.get())
    button7.configure(text = name.get())
    button8.configure(text = name.get())
    button9.configure(text = name.get())

name = StringVar()
name_entered = Entry(root, width=30, textvariable=name)
name_entered.pack()
name_entered.focus()


button0 = Button(frame, text='0', command=my_Click).grid(row=0, column=0)
button1 = Button(frame, text='1', command=my_Click).grid(row=0, column=1)
button2 = Button(frame, text='2', command=my_Click).grid(row=0, column=2)
button3 = Button(frame, text='3', command=my_Click).grid(row=1, column=0)
button4 = Button(frame, text='4', command=my_Click).grid(row=1, column=1)
button5 = Button(frame, text='5', command=my_Click).grid(row=1, column=2)
button6 = Button(frame, text='6', command=my_Click).grid(row=2, column=0)
button7 = Button(frame, text='7', command=my_Click).grid(row=2, column=1)
button8 = Button(frame, text='8', command=my_Click).grid(row=2, column=2)
button9 = Button(frame, text='9', command=my_Click).grid(row=3, column=1)

root.mainloop()
