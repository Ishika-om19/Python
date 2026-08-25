# Functions & Modules

def Inputbooks():
    global bookname,auname,price,publishers
    bookname=input("Enter Book Name :").strip().title()
    auname=input("Enter Author Name :").strip().title()
    price=int(input("Enter Price :"))
    publishers=input("Enter Publisher Name :").strip().title()

def Showbooks():
    print("Book Name = ", bookname)
    print("Author Name = ", auname)
    print("Price = ", price)
    print("Publisher Name = ", publishers)
