# ----------------------------------------Listing files in AWS Resource Start--------------------------------------------------------------

import boto3

resource = boto3.resource('s3')

response = resource.Bucket('2023-bucket.log')

print("Listing bucket files or objects")

for res in response.objects.all():
    print(res.key)

# ----------------------------------------Listing files in AWS Resource End--------------------------------------------------------------
