#1st List Example

regcourse= ["BCA","BBA","B.Tech","MCA","M.Tech","B.Com","BA"]
others= ["MBA","LLB","Cyber Security","AWS","Oracle"]
#Merging of two Lists
allcourse= regcourse + others
#append() is used for add element at the end of list
allcourse.append("AI")
#used for insert new elements
allcourse.insert(2,"Pyton Training")
#used for remove list elements
allcourse.remove("LLB")
#Sorting in Accending order
allcourse.sort()
print("List of All Courses")
for x in allcourse:
    print(x)
#length shows all the elements numaber of List
print("Total No of Courses = ",len(allcourse))

#Crearing A Blank List
collegecourse=[]
for x in allcourse:
    collegecourse.append(x.upper())

#Code for searching

c=input("Enter the course:").strip().upper()
if c in collegecourse:
    print(f"{c} course is available")
else:
    print(f"{c} course is not available")

#del is used for delete List
del allcourse
