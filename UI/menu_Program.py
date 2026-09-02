#Implementing Menu
from tkinter import *
import sys
def red():
    root.configure(bg="red")
def green():
    root.configure(bg="green")
def orange():
    root.configure(bg="orange")
def pink():
    root.configure(bg="pink")
def stop():
    root.destroy()
    #sys.exit()
    
root=Tk()
mainmenu = Menu(root)#Creating a Menu Bar
root.title('Color Window')
m1 = Menu(mainmenu, tearoff=0)#tearoff=0 just not to show any other extra item
m1.add_command(label="Red", command=red)
m1.add_separator()
m1.add_command(label="Green", command=green)
m1.add_separator()#To Make A Horizontal Line within the Menu
m1.add_command(label="Orange",command=orange)
m1.add_separator()
m1.add_command(label="Pink",command=pink)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Color", menu=m1)
mainmenu.add_command(label="Exit",command=stop)
mainmenu.add_cascade(label="others")
root.config(menu=mainmenu)
root.mainloop()
