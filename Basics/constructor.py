#Constructor

class book:
    def __init__(myobj, pubs="BPB"):
        #myobj.publisher="BPB"
        myobj.publisher=pubs

    def Inputbooks(myobj):
        myobj.bookname=input("Enter Book Name : ").strip().title()
        myobj.auname=input("Enter Author Name : ").strip().title()
        myobj.price=int(input("Enter Price : "))

    def Showbooks(myobj):
        print("Book Name = ", myobj.bookname)
        print("Author Name = ", myobj.auname)
        print("Price = ", myobj.price)
        print("Publisher Name = ", myobj.publisher)

    def Storefile(myobj):
        myfile=open("C:\\PyTraining\\Basics\\BookList.csv","a")
        data=myobj.bookname+","+myobj.auname+","+str(myobj.price)+","+myobj.publisher+"\n"
        myfile.write(data)
        myfile.close()
        print("Record Added Successfully")

book1=book()
book1.Inputbooks()
book1.Showbooks()
book1.Storefile()
book2=book("Panda")
book2.Inputbooks()
book2.Showbooks()
book2.Storefile()
print(type(book1))
print(type(book2))
del book1, book2
