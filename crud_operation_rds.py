import mysql.connector
import sam_config as config

config_master = {
'host' : config.rds_mysql['host'],
'user' : config.rds_mysql['user'],
'password' : config.rds_mysql['password'],
'database' : config.rds_mysql['database']
}

def connect_db(dbname, **config):
    try:
        cnx = mysql.connector.connect(**config)
        cur = cnx.cursor(dictionary=True)
        cnx.autocommit = True
        print(f"Database: {dbname} connected successfully")
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        exit(1)
    return (cnx, cur)

def close_db(dbname, slave):
    (cnx, cur) = slave
    cnx.close()
    cur.close()
    print(f"Database: {dbname} closed successfully")


(cnx, cur) = connect_db('[Database]', **config_master)

'''
#  to fetch records from db table

query = """select * FROM person"""
cur.execute(query)
result = cur.fetchall()

print(f"result: {result}")
'''


'''
# to insert data into db table

query = """Insert into person (name, lastname) values ("Dua", "Lipa")"""
cur.execute(query)

print("Data inserted into table successfully..")
'''


'''
# to delete records from db table

query = """Delete from person where id in (1,2,3,4,5,6,7,8,9,10,11,12,13,14)"""
cur.execute(query)

print("Delete data from table..")
'''


'''
# truncating db table to set id column from id = 1

query = """TRUNCATE TABLE person"""
cur.execute(query)

print("Truncated table successfully..")
'''


'''
# to update data in db table

query = """update person set name = 'Sambram', lastname = 'Heddurshetti' where id = 1"""
cur.execute(query)

print(f"query: {query}")

print("Updated data successfully..")
'''

close_db('[Database]', (cnx, cur))


'''
# Below codes describes mydb instance info


import boto3

from pprint import pprint

rds_client = boto3.client('rds')

response = rds_client.describe_db_instances(
    DBInstanceIdentifier = 'rdsdbtuts'
)

pprint(response)

'''