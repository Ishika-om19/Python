#Classes & Objects

class book:
    def Inputbooks(myobj):#When we make a function in class there always pass argument like myobj which stores object references 
        myobj.bookname=input("Enter Book Name : ").strip().title()
        myobj.auname=input("Enter Author Name : ").strip().title()
        myobj.price=int(input("Enter Price : "))
        myobj.publisher=input("Enter Publisher Name : ").strip().title()

    def Showbooks(myobj):#function made by 'def'
        print("Book Name = ",myobj.bookname)
        print("Author Name = ",myobj.auname)
        print("Price = ",myobj.price)
        print("Publisher Name = ",myobj.publisher)

    def Storefile(myobj):
        myfile=open("C:\\PyTraining\\Basics\\BookList.csv","a")#append Mode
        data=myobj.bookname+","+myobj.auname+","+str(myobj.price)+","+myobj.publisher+"\n"
        myfile.write(data)
        myfile.close()
        print("Record Added Successfully")

book1=book() #Object will be created
book1.Inputbooks() #book.Inputbooks(book1)
book1.Showbooks()
book1.Storefile()
print(type(book1))
del book1
