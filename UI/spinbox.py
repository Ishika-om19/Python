#How To Apply Spinbox in Python

from tkinter import *
def show():
    mylabel.config(text="Selected Value ="+spin.get())
top = Tk()
top.geometry("300x400")
spin = Spinbox(top, from_=0, to = 25,increment=1,command=show)
spin.pack()

mylabel=Label(top,"",bg="orange")
mylabel.pack()
top.mainloop()
