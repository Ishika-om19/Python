# Dictionary Creation
# Dictionary in Python are collection of key-value pairs, each key must be unique.
# Dictionary can be created by placing a sequence of elements with in curly{} braces, separated by comma.
studentlist={"AB54":("Ishika","BCA",175),
             "AB40":("Hariom","B.Tech",75),
             "AB55":("Issu","BCA",24),
             "AB60":("Om","B.Tech",21)}
print(type(studentlist))
print("Total number of students = ", len(studentlist))
print("Detail of student AB40 :")
print(studentlist.get("AB40"))
print("Detail of student AB54 :")
print(studentlist.get("AB54"))
print("Records of All students in dictionary :")
print(studentlist.items())

#Organized way of printing the Records of All key-value pair
#sorted() use to sort the dictionary items on key-value pair
print("All Records in sorted :")
for x in sorted(studentlist.keys()):
    print(x, studentlist.get(x))

#To sorted() in decending order we use reverse=True
print("Reverse of all Records:")
for x in sorted(studentlist.keys(),reverse=True):
    print(x, studentlist.get(x))

#adding key-value pair using update
print("After updation :")
newlist={"AB35": ("Arya","B.Tech",57),"AB57":("Janvi","BCA",55)}
studentlist.update(newlist)
for x in sorted(studentlist.keys()):
    print(x, studentlist.get(x))
