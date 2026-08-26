# Concept of Lambda
#Lambdas are also known as anonymous function 
#we use a keyword lambda to create our own lambda, normal function created by using def keyword

import math

findsqroot= lambda x: round(math.sqrt(x),2)
#myno= int(input("Enter A No : "))
#result= findsqroot(myno)
#print("Square Root of %d = %.2f" %(myno, result))
 
samplenos=[24,45,81,78,27,36,50,81,9]
result= map(findsqroot,samplenos)
print(tuple(result))
