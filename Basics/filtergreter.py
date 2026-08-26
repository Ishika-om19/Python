# Consider the following list of Nos and seggregate the Nos
#Basis on >= 50 or Not

marks=[45,97,60,89,38,64,71,61,42,47,53]

mygreterlist= lambda x: (x >= 50)
mylesslist= lambda y: not (y >= 50)
grelist= filter(mygreterlist, marks)
lesslist= filter(mylesslist, marks)
print("Greater then And Equal to 50:")
print(list(grelist))

print("Less then 50:")
print(list(lesslist))
