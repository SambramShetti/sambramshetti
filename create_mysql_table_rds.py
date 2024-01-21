'''
Below code is used to create mysql table in rds
'''

# import mysql.connector as mc

# try:
#     mydb = mc.connect(
#         host="rdsdbtuts.cpqus8g8mwjs.ap-south-1.rds.amazonaws.com",
#         user="admins",
#         password="password",
#         database='dbtuts'
#     )

#     cur = mydb.cursor()

#     query = "create table person (id int auto_increment primary key, name varchar(300), lastname varchar(300))"
#     cur.execute(query)
#     print(f"query: {query}")
#     print("Table created")
# except Exception as e:
#     print("Failed db connection:", e)



'''
Below codes are used to show database tables in rds
'''

import mysql.connector as mc


try:
    mydb = mc.connect(
        host="rdsdbtuts.cpqus8g8mwjs.ap-south-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database='dbtuts'
    )

    cur = mydb.cursor()

    cur.execute("SHOW TABLES")
    for table in cur:
        print(table)

except Exception as e:
    print("No such database:", e)
        

