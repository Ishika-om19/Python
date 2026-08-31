from tkinter import *
from tkinter import ttk
import tkinter as tk

mywin=Tk()#this line creating window mywin.title("New Window")
mywin.title("New Window")
mywin.geometry("400x400")
mywin.config(bg="black")

label1 = ttk.Label(mywin, text="Enter Your Name")#Creating a Label
text1 = ttk.Entry (mywin) #Creates An Edit Box
label1.pack()
text1.pack() #To Make the controlVisible

label2 = ttk.Label(mywin, text="Enter your Mobile No")#Creating a Label
text2 = ttk.Entry(mywin) #Creates An Edit Box
label2.pack()
text2.pack()

label3 = tk.Label(mywin, text="Enter Your Location", fg="Green")#Creating a Lable 
citylist = ["New Delhi", "Meerut", "Ghaziabad", "Bhopal", "Kanpur", "Noida"]
mylist = ttk.Combobox(mywin,values=citylist)
label3.pack()
mylist.pack()
mywin.mainloop()
