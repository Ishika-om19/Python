#program to count no of words
#we are learning python

myline=input("Enter the sentence :").strip()
words=myline.split(" ")
print(words)
print("Total No of Words = ", len(words))
