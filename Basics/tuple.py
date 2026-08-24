#Tuple Related Problems

courses=("BCA","MBA","BA","B.Tech","B.Com","B.Sc.","B.Pharma")

#Tuple can't sort so,courses.sort() give error but tuple can sorted(courses) worked
print("Our courses before updation")
for y in sorted(courses) :
    print(y)
newcourse= list(courses)
newcourse.append("BioTech")
newcourse.sort()
for x in newcourse:
    if x=="MBA":
        x="MBA Finance"
        newcourse.remove("MBA")
        newcourse.append(x)
        
courses= tuple(newcourse)
print("Our Updated courses are :")
for x in courses :
    print(x)

#Creating a blank tuple
mytuple=()
print(type(mytuple))
oldtuple=("Shoes","T-shirt","Jacket")
mytuple+= oldtuple
print(mytuple)
#if you try to make tuple like addtuple=("book") it will not worked add comma after quotes
addtuple=("book",)
mytuple+= addtuple
print(mytuple)
