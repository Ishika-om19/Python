# Set Operations

TeamA={"Ishika","Om","Hari","Harish"}
TeamB={"Om","Hari","Ishika","Harish"}

if(TeamA==TeamB):
    print("Same Team is there")
else:
    print("Team is Different")
print(type(TeamA))

#to add any element we using add function in set , set doesn't follow any order
TeamA.add("Hariom")
print(TeamA)

#to make blank set
myset= set()#set
print(type(myset))

newset= {}#dictionary
print(type(newset))
