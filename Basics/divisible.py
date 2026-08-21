#The number is divisible by the 5 and 8

num= int(input("Enter the number : "))
result1= num % 5
result2= num % 8
if(result1==0 and result2==0):
    print("%d is Divisible By both 5 and 8" %num)
elif(result1!=0 and result2==0):
    print("%d is Divisible By 8 but not by 5" %num)
elif(result1==0 and result2!=0):
    print("%d is Divisible By 5 but not by 8" %num)
elif(result1!=0 and result2!=0):
    print("%d is Not Divisible By 5 and 8 " %num)

    print("program Ended")
