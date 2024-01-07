# ----------------------------------------Copying object from 1 bucket to another in AWS Resource Start--------------------------------------------------------------

import boto3

resource = boto3.resource('s3')

copy_source = {
    'Bucket' : '2023-bucket.log', # from which bucket we want to copy file
    'Key' : 'image.jpg'
}

bucket = resource.Bucket('unique123-pythons') # in which bucket we want to copy file
obj = bucket.Object('copied_file.jpg') # name for copied file
obj.copy(copy_source)

# ----------------------------------------Copying object from 1 bucket to another in AWS Resource End--------------------------------------------------------------
