# -------------------------------------Client Listing Bucket Objects Start-------------------------------------------------------

# import boto3

# client = boto3.client('s3')

# response = client.list_buckets()

# print("Listing all buckets")

# bucket = [i['Name'] for i in response['Buckets']]
# print(f"Bucket: {bucket}")

# -------------------------------------Client Listing Bucket Objects End-------------------------------------------------------


# -------------------------------------Response Listing Bucket Objects Start-------------------------------------------------------

import boto3

resource = boto3.resource('s3')

response = resource.buckets.all()

print("Listing all buckets")

bucket = [i.name for i in response]

print(f"bucket: {bucket}")

# -------------------------------------Response Listing Bucket Objects End-------------------------------------------------------
