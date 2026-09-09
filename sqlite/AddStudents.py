import sqlite3 #This Module will only work for sqlite
try:
    conn = sqlite3.connect('mydatabase') #Connection with the Database
    cur = conn.cursor() #Adding A Record in ItemMaster Table
    roll = input("Enter Roll NO:").strip().upper()
    sname = input("Enter Student Name:").title().strip()
    cname = input("Course Name: ").title().strip()
    fees = int(input("Enter fees:"))
    sqlstatement = ("insert into Students values(?,?,?,?)") #? For Parameters
    mytuple = (roll,sname,cname,fees)#tuple
    cur.execute(sqlstatement,mytuple)
    conn.commit() #Then Only Record will be Saved within the Table
    print("Record Added Successfully")
except sqlite3.OperationalError:
    print("Sorry DataBase Connectivity Failed")
except sqlite3.IntegrityError as err:
    print("Some Criteria Not Ful Filled...")
    print(err)
except Exception as e:
    print(e)
    print("Record Could NOt Be Added")
finally:
    conn.close()
