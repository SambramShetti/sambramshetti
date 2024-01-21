import boto3

client = boto3.client('rds')

'''
# This block of code is used to describe db instance

desc_response = client.describe_db_instances(
    DBInstanceIdentifier='rdsdbtuts',
)

print(desc_response)
'''


'''
# This block of code is used to delete db instance

delete_response = response = client.delete_db_instance(
    DBInstanceIdentifier='rdsdbtuts',
    SkipFinalSnapshot=False,
    FinalDBSnapshotIdentifier='string',
    DeleteAutomatedBackups=True
)

print(delete_response)
'''