import tkinter as tk
from tkinter import ttk

def addition(ev):
    firstno=int(entry1.get())#.get()=value read karta hai
    secondno=int(entry2.get())
    result=firstno+secondno
    entry3.insert(0,str(result))#.insert()=value add karta hai

def subtraction(ev):
    firstno=int(entry1.get())
    secondno=int(entry2.get())
    result=firstno-secondno
    entry3.insert(0,str(result))

def multiply(ev):
    firstno=int(entry1.get())
    secondno=int(entry2.get())
    result=firstno*secondno
    entry3.insert(0,str(result))

def divide(ev):
    firstno=int(entry1.get())
    secondno=int(entry2.get())
    result=round(firstno/secondno,2)
    entry3.insert(0,str(result))

def clear(ev):
    entry1.delete(0,tk.END)#.delete()=value remove karta hai
    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)

root = tk.Tk() #Creating Window
root.title("My First GUI")
root.configure(bg="light green")
label1 = ttk.Label(root, text="First No")
entry1 = ttk.Entry(root)
label2 = ttk.Label(root, text="Second No")
entry2 = ttk.Entry(root)

label3 = ttk.Label(root, text="Result")
entry3 = ttk.Entry(root)
btn1 = ttk.Button(root, text="Add")
btn2 = ttk.Button(root, text="Subtract")
btn3 = ttk.Button(root, text="Multiply")
btn4 = ttk.Button(root, text="Divide")
btn5 = ttk.Button(root, text="Clear")

label1.grid(row=0, column=0, padx=5, pady=10)
entry1.grid(row=0, column=1, padx=5, pady=10)
label2.grid(row=1, column=0, padx=5, pady=10)
entry2.grid(row=1, column=1, padx=5, pady=10)
label3.grid(row=2, column=0, padx=5, pady=10)
entry3.grid(row=2, column=1, padx=5, pady=10)
btn1.grid(row=3, column=0, padx=5, pady=20)
btn2.grid(row=3, column=1, padx=5, pady=20)
btn3.grid(row=4, column=0, padx=10, pady=20)
btn4.grid(row=4, column=1, padx=10, pady=20)
btn5.grid(row=5, column=0, padx=10, pady=20)

btn1.bind("<Button>", addition)
btn2.bind("<Button>", subtraction)
btn3.bind("<Button>", multiply)
btn4.bind("<Button>", divide)
btn5.bind("<Button>", clear)


root.geometry("350x400") #root.geometry("widthxheigth")
root.mainloop() #Now Events can be captured
