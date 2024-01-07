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
