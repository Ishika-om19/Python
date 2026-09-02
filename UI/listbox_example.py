#Example of A List Box

import tkinter as tk
from tkinter import ttk
def show_selected(ev):
    selected = mylist.get(mylist.curselection())
    mywin.configure(bg=selected)
mywin=tk.Tk()
mywin.title("ListBox Example")
mywin.geometry("400x350")
mylist=tk.Listbox(mywin)
mylist.insert(1,"Red")
mylist.insert(2,"Blue")
mylist.insert(3,"Yellow")
mylist.insert(4,"Magenta")
mylist.insert(5,"Purple")
mylist.delete(0)#deletion using zero based indexing 
mylist.bind("<<ListboxSelect>>",show_selected)
mylist.pack()
mywin.mainloop()
