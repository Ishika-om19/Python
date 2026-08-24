#Webinar Example
studentlist=["ishika.bca.2024@mitmeerut.ac.in","chandrika.bca.2024@mitmeerut.ac.in","kajal.bca.2024@mitmeerut.ac.in","tanu.bca.2024@mitmeerut.ac.in","hariom.kumar.btech.2024@mitmeerut.ac.in","om.btech.2024@mitmerut.ac.in","issu.bca.2024@mitmeerut.ac.in","ishika.bca.2024@mitmeerut.ac.in","hariom.kumar.btech.2024@mitmeerut.ac.in","issu.bca.2024@mitmeerut.ac.in"]
emailid=set(studentlist)
print("List of Participants")
for x in emailid:
    print(x)

print("Actual Participants = %d" %len(emailid))#Set Need only unique values
