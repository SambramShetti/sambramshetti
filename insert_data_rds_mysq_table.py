import mysql.connector as mc


try:
    mydb = mc.connect(
        host="rdsdbtuts.cpqus8g8mwjs.ap-south-1.rds.amazonaws.com",
        user="admins",
        password="password",
        database='dbtuts'
    )

    cur = mydb.cursor()

    query = """insert into person (name, lastname) values ('sam', 'John')"""
    # query = """select * from person"""
    cur.execute(query)
    mydb.commit()
    for table in cur:
        print(table)

except Exception as e:
    print("No such database:", e)