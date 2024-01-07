# ----------------------------------------Download files in AWS Resource Start--------------------------------------------------------------

import boto3

resource = boto3.resource('s3')

# response = resource.meta.client.download_file('2023-bucket.log', 'image.jpg', 'D:\image.jpg') # 1st approach
response = resource.Bucket('2023-bucket.log').download_file('Jnr_software_resume.pdf', 'D:\Jnr_software_resume.pdf')  # 2nd approach

print(f"response: {response}")


# ----------------------------------------Download files in AWS Resource End--------------------------------------------------------------
