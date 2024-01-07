# -------------------------------------Response Bucket Start-------------------------------------------------------

'''
below codes are for creating bucket in AWS for resource
'''

# import boto3

# bucket = boto3.resource('s3')

# response = bucket.create_bucket(
#     ACL='private',
#     Bucket = 'botolesson',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-south-1'}

# )

# print(f"response: {response}")

# -------------------------------------Response Bucket End-------------------------------------------------------



# -------------------------------------Client Bucket Start-------------------------------------------------------

'''
below codes are for creating bucket in AWS for client
'''

import boto3

bucket = boto3.client('s3')

response = bucket.create_bucket(
    ACL='private',
    Bucket='unique123-pythons',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'}
)
print(f"response: {response}")

# -------------------------------------Client Bucket End-------------------------------------------------------
