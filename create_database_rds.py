'''
This block of code is used to connect to aws mysql db.

'''

import mysql.connector as mc

try:
    mydb = mc.connect(
        host="rdsdbtuts.cpqus8g8mwjs.ap-south-1.rds.amazonaws.com",
        user="admins",
        password="password"
    )

    # print("Connected")
    dbname = input("Please enter your db name: ")  # Fixed input prompt
    cur = mydb.cursor()

    cur.execute(f"CREATE DATABASE {dbname}")  # Corrected SQL statement

    print("Database created")

except mc.Error as e:
    print("Failed db connection:", e)
