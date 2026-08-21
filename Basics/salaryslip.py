#Example to while loop

while True:
    empname= input("Enter Employee Name:")
    basicsal= int(input("Enter Basic Salary:"))
    hra= basicsal * .1
    da= basicsal * .2
    netSalary= basicsal + hra + da
    print("SALARY SLIP GENERATED")
    print("*********************")
    print("Name = %s" %empname)
    print("Total Salary = %.2f" %netSalary)
    choice= input("Want to continue? Say Yes!!!!!!")
    if(choice=="Yes" or choice=="yes"):
        continue
    else:
        break
print("End of Program")
