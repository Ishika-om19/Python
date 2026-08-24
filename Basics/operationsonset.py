#Major Operatiions on Set

pricorus={"Sales","IT","CSO","FSO","LDM"}

symphony={"Sales","CSO","Purchase","HR","Admin"}

#symmphony has procured pricorous
newdepts=pricorus - symphony #Finding the Difference
print("New Depts To Be Formed")
print(newdepts)
print("Total New Depts = %d " %(len(newdepts)))

cdept=pricorus & symphony # & stands for intersection
print("Common Depts To Be Formed")
print(cdept)
print("Total Common Depts = %d " %(len(cdept)))

alldepts=symphony | pricorus #|means Union
print("Overall Depts Are")
print(alldepts)
print("Total Depts=%d" %len(alldepts))
