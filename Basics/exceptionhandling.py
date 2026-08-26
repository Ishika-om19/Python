#Exception Handlings

try:
    firstno= int(input("Enter First No:"))
    secondno= int(input("Enter Second No:"))
    result= firstno / (secondno - 3)
    print("Total = %.2f" %result)
# Special Exception Handler ex- ValueError,ZeroDivisionError etc.
except ValueError:
    print("Exception Raised due to Improper Values")
except ZeroDivisionError:
    print("Sorry Division by 0 is Not Possible...Do not use 3 as second No")
#Default Exception Handler
except Exception as reason:
    print("Sorry some exception came")

finally:
    print("Thanks")
