#First Program For DataBase Connectivity

import sqlite3
try:
    conn = sqlite3.connect('mydatabase') #Connection Object
    cur = conn.cursor() #Creating the Cursor Object
    cur.execute("SELECT * FROM Students")
    count = 0

    print('List of Students::')
    #print(cur.description)
    for row in cur :
        print(row)
        count+=1
    print("All Rows Displayed")
    print("Total Records = %d" %(count))
except sqlite3.OperationalError: #In case there is Connectivity Issue
    print("Error...Please Check Table Name or Database")
except:
    print("DataBase Connectivity Failed...Sorry Try Later")
finally:
    conn.close() #Closing the Connection Object
    print("Thanks for Using this Application")
