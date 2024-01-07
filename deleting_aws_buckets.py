# -------------------------------------Client Deleting Empty Bucket Start-------------------------------------------------------

# import boto3

# client = boto3.client('s3')

# response = client.delete_bucket(
#     Bucket = 'unique123-pythons'
# )

# print(f"response: {response}")

# -------------------------------------Client Deleting Empty Bucket End-------------------------------------------------------



# -------------------------------------Response Deleting Empty Bucket Start-------------------------------------------------------

# import boto3

# resource =  boto3.resource('s3')

# Bucket = 'unique123-pythons'
# response = resource.Bucket(Bucket)

# response.delete()

# print(f"Bucket {response} has been deleted")

# -------------------------------------Response Deleting Empty Bucket End-------------------------------------------------------





# -------------------------------------Response Deleting Non-Empty Bucket Start-------------------------------------------------------

import boto3

resource = boto3.resource('s3')

response = resource.Bucket('sambram-boto-bucket')

def clean_up():

    # delete the object
    for i in response.objects.all():
        i.delete()


    # delete the bucket versoning
    for j in response.object_versions.all():
        j.delete()
    
    print("Cleaned s3 bucket")

clean_up()

response.delete()

print("Deleted s3 bucket")

# -------------------------------------Response Deleting Non-Empty Bucket End-------------------------------------------------------
