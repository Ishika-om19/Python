#Example of filters

studentlist=["ishika.bca.2024@mitmeerut.ac.in","chandrika.bca.2024@gmail.com","kajal.bca.2024@gmail.com","tanu.bca.2024@gmail.com","hariom.kumar.btech.2024@mitmeerut.ac.in","om.btech.2024@mitmerut.ac.in","issu.bca.2024@mitmeerut.ac.in","ishika.bca.2024@mitmeerut.ac.in","hariom.kumar.btech.2024@gmail.com","issu.bca.2024@gmail.com"]

mitlist=lambda x: x.endswith("@mitmeerut.ac.in")
outerlist=lambda y: not y.endswith("@mitmeerut.ac.in")
mitstudents=filter(mitlist, studentlist)
nonmit=filter(outerlist, studentlist)
print("EMail IDs From MIT:")
print(list(mitstudents))

print("EMail IDs Outside MIT:")
print(list(nonmit))
