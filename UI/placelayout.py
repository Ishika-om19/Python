import tkinter as tk
from tkinter import ttk

root = tk.Tk() #Creating Window
root.title("My First GUI")
root.configure(bg="Light blue")

# To change the icon at window 
#root.iconbitmap("myicon.png")
myicon=tk.PhotoImage(file="myicon.png")
root.iconphoto(True,myicon)
label1 = ttk.Label(root,text="Enter your Name")
entry1 = ttk.Entry(root)
label1.place(x=50,y=100)
entry1.place(x=250,y=100)
label2 = ttk.Label(root,text="Enter contact No")
entry2 = ttk.Entry(root)
label2.place(x=50,y=200)
entry2.place(x=250,y=200)
root.mainloop()
