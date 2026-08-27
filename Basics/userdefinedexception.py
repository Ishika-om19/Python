# Creating Usker Defined Exception

class BlankNameException(Exception):
    pass
class InvalidSalaryException(Exception):
    pass

try:

    empname = input("Enter Employee Name :").strip().upper()
    if(len(empname)==0):
        raise BlankNameException
    basicsal=int(input("Enter Basic Salary :"))
    if(basicsal < 2500):
        raise InvalidSalaryException
    print("Employee Name = ", empname)
    print("Salary =", basicsal)

except ValueError:
    print("Sorry Not A Number")
except BlankNameException:
    print("Sorry Name is Blank")
except InvalidSalaryException:
    print("Invalid Salary...At least 25000")

except Exception as p1:
    print("Sorry Exception Due To ", p1)

finally:
    print("End the program")
    
