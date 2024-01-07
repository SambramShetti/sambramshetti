# ----------------------------------------Getting object summary in AWS Resource Start--------------------------------------------------------------

import boto3

resource = boto3.resource('s3')

obj_summary = resource.ObjectSummary('2023-bucket.log', 'image.jpg')

# print(f"obj_summary: {obj_summary}")
print(f"obj_summary: {obj_summary.bucket_name}")

# ----------------------------------------Getting object summary in AWS Resource End--------------------------------------------------------------