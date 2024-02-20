# -------------------------------------Client Bucket upload object Start-------------------------------------------------------

# import boto3

# client = boto3.client('s3')

# response = client.put_object(
#     ACL='private',
#     Body=b'bytes',
#     Bucket='2023-bucket.log',
#     Key='image.jpg'
# )

# print(f"response: {response}")

# -------------------------------------Client Bucket upload object End-------------------------------------------------------

# -------------------------------------Client Bucket upload object Start Approach 2-------------------------------------------------------

import boto3

client = boto3.client('s3')

with open ("E:\Pictures\I_me_myself\image (2).jpg", "rb") as f:
    data = f.read()

response = client.put_object(
    ACL='private',
    Body=data,
    Bucket='sambram-boto-bucket',
    Key='image (2).jpg'
)

print(f"response: {response}")

# -------------------------------------Client Bucket upload object End Approach 2-------------------------------------------------------


# -------------------------------------Resource Bucket upload object Start-------------------------------------------------------

import boto3

s3_resource = boto3.resource('s3')

bucket_name = 'bucket-20feb2024-resource'
key = 'Screenshot (535).png'

# Select the bucket using the resource
bucket = s3_resource.Bucket(bucket_name)

# Upload the object to the bucket
response = bucket.put_object(
    ACL='private',
    Body=b'bytes',
    Key=key
)

print("response: ", response)
# -------------------------------------Resource Bucket upload object End-------------------------------------------------------
