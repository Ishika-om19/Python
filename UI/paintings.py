import tkinter as tk
from tkinter import ttk

mywin=tk.Tk()
mywin.geometry("400x500")
mywin.title("New Graphics")

canvas=tk.Canvas(mywin,width=400,height=500)
canvas.pack()
canvas.create_line(30,30,100,100,fill="gray",width=9)
canvas.create_rectangle(70,160,150,210, fill="purple",width=3)
canvas.create_oval(190,220,350,310, fill="pink",width=3)
canvas.create_rectangle(200,400,300,500, fill="pink",width=4)

