# First Program For DataBase Connectivity(pandas)
import sqlite3
import pandas as pd
try:
    conn = sqlite3.connect('mydatabase') # Connection object
    #cur = conn.cursor() #Creating the Cursor Object
    cur = pd.read_sql_query("SELECT * FROM Students",conn)
    print("All Rows Displayd")
    print(cur)
    print("Total Fees = %d" %cur['Fees'].sum())
    print("Total No of Students = %d" %cur['Rollno'].count())
except sqlite3.OperationalError: #In case there is Connectivity Issue
    print("Error...Please Check Table Name or Database")
except Exception as k:
    print("Exception..."+k)
finally:
    conn.close() #Closing the connection object
    print("Thanks for using this Application")
        
