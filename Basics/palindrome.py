str=input("Enter a string to chect wether it is palindrom or not :").strip().upper()
rev= str[::-1]

if str == rev :
    print ("palindrom")
else :
    print("NOt palindrom")
