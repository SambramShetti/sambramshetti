'''
This block of codes is used for rds connection.
Like creating database.

documentation link: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_instance.html 
'''

import boto3
from pprint import pprint

rds_client = boto3.client('rds')

response = rds_client.create_db_instance(
    DBName = "dbtuts",
    DBInstanceIdentifier = "rdsdbtuts",
    AllocatedStorage = 20,
    DBInstanceClass = "db.t2.micro",
    Engine = "MySQL",
    MasterUsername = "admins",
    MasterUserPassword = "password",
    Port = 3306,
    EngineVersion = "8.0.35",
    PubliclyAccessible = True,
    StorageType = 'gp2'   
)

pprint(response)