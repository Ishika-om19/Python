import tkinter as tk
from tkinter import ttk
import turtle
mywin=tk.Tk()
mywin.title("Canvas Example")
mywin.geometry("400x350")

mycanvas=tk.Canvas(mywin,width=400,height=400)
mycanvas.pack()
mycanvas.create_rectangle(60,60,100,100,outline="black",fill="green",width=3)
mycanvas.create_oval(100,200,200,300,outline="black",fill="yellow",width=3)
mywin.mainloop()
