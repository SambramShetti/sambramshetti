# ----------------------------------------Delete object from aws bucket client Start--------------------------------------------------------------

import boto3

client = boto3.client('s3')

'''
# deleting only 1 object/file from bucket

del_obj = client.delete_object(
    Bucket='unique123-pythons', # bucket_name
    Key='copied_file', # file_name
)

print(f"del_obj: {del_obj}")

'''
# Deleting multiple objects/files from bucket

response = client.delete_objects(
    Bucket='2023-bucket.log',
    Delete={
        'Objects': [
            {
                'Key': 'Jnr_software_resume.docx',
            },
            {
             'Key': 'Jnr_software_resume.pdf',   
            }
        ],
    }
)

print(f"response: {response}")
# ----------------------------------------Delete object from aws bucket client End--------------------------------------------------------------


'''
this block of codes is used to delete specified bucket policy



import boto3

client = boto3.client('s3')

response = client.delete_bucket_policy(
    Bucket = "2023-bucket.log"
)

print(f"response: {response}")

'''