# ----------------------------------------Listing filtered files in AWS Resource Start--------------------------------------------------------------

# this will fetch only selected file from aws s3 bucket

import boto3

resource = boto3.resource('s3')

response = resource.Bucket('2023-bucket.log')

print("Listing bucket filtered files or objects")

# for res in response.objects.filter(Prefix='image.jpg'):
for res in response.objects.filter(Prefix='Jnr_software_resume'):
    print(res.key)

# ----------------------------------------Listing filtered files in AWS Resource End--------------------------------------------------------------
