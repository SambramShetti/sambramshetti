# ----------------------------------------Listing files in AWS Resource Start--------------------------------------------------------------

import boto3

resource = boto3.resource('s3')

response = resource.Bucket('2023-bucket.log')

print("Listing bucket files or objects")

for res in response.objects.all():
    print(res.key)

# ----------------------------------------Listing files in AWS Resource End--------------------------------------------------------------



# ----------------------------------------Listing files in AWS Client Start--------------------------------------------------------------

import boto3

client = boto3.client('s3')

response = client.list_objects(
    Bucket='bucket-20feb2024',
)

for i in response['Contents']:
    print("response: ", i['Key'])

# ----------------------------------------Listing files in AWS Client End--------------------------------------------------------------
